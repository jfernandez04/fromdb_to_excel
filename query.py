# coding=utf-8
q = """select * from (SELECT oe.idorden_embarque,
        `prod_orden_despacho`.`planilla` AS `embarque`,
        `oe`.`folio` AS `referencia`,
        `prod_conf_tipo_nave`.`codigo` AS `codigo_tipo_nave`,
        `prod_conf_tipo_nave`.`descripcion` AS `nombre_tipo_nave`,
        `base_nombrenave`.`nombre` AS `nombre_nave`,
        `base_recibidor`.`codigo` AS `codigo_recibidor`,
        `base_recibidor`.`nombre` AS `nombre_recibidor`,
        `prod_conf_agente_aduana`.`codigo` AS `codigo_agente_aduana`,
        `prod_conf_agente_aduana`.`nombre` AS `nombre_agente_aduana`,
        `prod_conf_embarcador`.`codigo` AS `codigo_embarcador`,
        `prod_conf_embarcador`.`nombre` AS `nombre_embarcador`,
        `base_exportador`.`codigo` AS `codigo_exportador`,
        `base_exportador`.`nombre` AS `nombre_exportador`,
        `base_pais`.`codigo` AS `codigo_pais`,
        `base_pais`.`nombre` AS `nombre_pais`,
        `puerto_origen`.`codigo` AS `codigo_puerto_origen`,
        `puerto_origen`.`descripcion` AS `nombre_puerto_origen`,
        `puerto_destino`.`codigo` AS `codigo_puerto_destino`,
        `puerto_destino`.`descripcion` AS `nombre_puerto_destino`,
        `base_naviera`.`codigo` AS `codigo_naviera`,
        `base_naviera`.`nombre` AS `nombre_naviera`,
        `base_nave`.`booking` AS `booking`,
        `base_nave`.`stacking` AS `stacking`,
        `base_nave`.`stacking_hasta` AS `stacking_hasta`,
        `base_nave`.`corte_documental` AS `corte_documental`,
        `oe`.`dus` AS `dus`,
        `oe`.`fitosanitario` AS `fitosanitario`,
        `oe`.`bl` AS `bl`,
        `prod_orden_despacho`.`guia_despacho` AS `guia_despacho`,
        `prod_orden_despacho`.`folio_sag` AS `folio_sag`,
        `prod_orden_despacho`.`fecha` AS `fecha`,
        `prod_orden_despacho`.`hora` AS `hora`,
        CONCAT(`cc_conf_empresa_transporte`.`rut`,
                '-',
                `cc_conf_empresa_transporte`.`razon_social`) AS `empresa_transporte`,
        `prod_orden_despacho`.`chofer` AS `nombre_chofer`,
        `prod_orden_despacho`.`rut_chofer` AS `rut_chofer`,
        IFNULL(`cc_transporte`.`fono_chofer`,
                `prod_orden_despacho`.`fono_chofer`) AS `fono_chofer`,
        `prod_orden_despacho`.`patente` AS `patente`,
        `prod_orden_despacho`.`patente_carro` AS `patente_carro`,
        `base_contenedor`.`contenedor` AS `contenedor`,
        `prod_orden_despacho`.`estado` AS `estado`,
        `prod_orden_despacho`.`ubicacion_sello` AS `ubicacion_sello`,
        `base_productor`.`codigo` AS `codigo_productor`,
        `base_productor`.`nombre` AS `nombre_productor`,
        `prod_etiquetado`.`codigo` AS `codigo_productor_etiquetado`,
        `prod_etiquetado`.`nombre` AS `nombre_productor_etiquetado`,
        `prod_conf_envase_operacional`.`peso_etiquetado` AS `peso_etiquetado`,
        `prod_conf_packing`.`codigo` AS `codigo_packing`,
        `prod_conf_packing`.`descripcion` AS `nombre_packing`,
        `prod_conf_frio`.`codigo` AS `codigo_frio`,
        `prod_conf_frio`.`descripcion` AS `nombre_frio`,
        `mercado_uno`.`codigo` AS `codigo_mercado_uno`,
        `mercado_uno`.`descripcion` AS `nombre_mercado_uno`,
        `mercado_dos`.`codigo` AS `codigo_mercado_dos`,
        `mercado_dos`.`descripcion` AS `nombre_mercado_dos`,
        `mercado_tres`.`codigo` AS `codigo_mercado_tres`,
        `mercado_tres`.`descripcion` AS `nombre_mercado_tres`,
        `mercado_cuatro`.`codigo` AS `codigo_mercado_cuatro`,
        `mercado_cuatro`.`descripcion` AS `nombre_mercado_cuatro`,
        `prod_orden_despacho_detalle`.`contramuestra` AS `contramuestra`,
        `prod_orden_despacho_detalle`.`termografo` AS `termografo`,
        `prod_existencia`.`folio` AS `folio`,
        `prod_conf_especie`.`codigo` AS `codigo_especie`,
        `prod_conf_especie`.`nombre` AS `nombre_especie`,
        `vari`.`codigo_variedad` AS `codigo_variedad`,
        `vari`.`descripcion` AS `nombre_variedad`,
        `varieti`.`codigo_variedad` AS `codigo_variedadeti`,
        `varieti`.`descripcion` AS `nombre_variedadeti`,
        `prod_conf_predio`.`codigo_csg` AS `nombre_predio`,
        `prod_conf_cuartel`.`descripcion` AS `nombre_cuartel`,
        `prod_conf_etiqueta`.`codigo` AS `nombre_etiqueta`,
        `prod_conf_envase_operacional`.`codigo` AS `codigo_envase_operacional`,
        `prod_conf_plu`.`codigo` AS `nombre_plu`,
        `base_categoria`.`codigo` AS `nombre_categoria`,
        `prod_conf_base_pallet`.`codigo` AS `nombre_base_pallet`,
        `prod_conf_tipo_tratamiento`.`codigo` AS `nombre_tipo_tratamiento`,
        `prod_conf_calibre`.`codigo` AS `nombre_calibre`,
        `prod_existencia`.`altura` AS `altura`,
        `prod_existencia`.`condicion` AS `condicion`,
        `prod_existencia`.`total_caja` AS `total_caja`,
        ((`prod_existencia`.`total_caja` * `prod_conf_envase_operacional`.`peso_etiquetado`) / `envope_especie`.`peso_etiquetado`) AS `cajas_equivalentes`,
        `prod_existencia`.`temperatura` AS `temperatura`,
        `prod_existencia`.`fecha_packing` AS `fecha_packing`,
        (CASE `prod_existencia`.`activo`
            WHEN 1 THEN 'Disponible'
            WHEN 2 THEN 'Asignado'
            ELSE 'No Existe'
        END) AS `nombre_activo`,
        (CASE `prod_existencia`.`estado_sag`
            WHEN 'I' THEN 'Inspección'
            WHEN 'O' THEN 'Origen'
            WHEN 'U' THEN 'Inspección USDA'
            WHEN 'R' THEN 'Rechazado'
            WHEN 'SC' THEN 'Sin condición'
            WHEN 'SF' THEN 'Fumigado'
            WHEN 'AN' THEN 'Anulado'
        END) AS `nombre_estado_sag`,
        (CASE `prod_existencia`.`idtipo`
            WHEN 1 THEN 'Saldo'
            WHEN 2 THEN 'pallet'
        END) AS `tipo`,
        `prod_conf_envase_operacional`.`peso_neto` AS `peso_neto`,
        (CASE `prod_existencia`.`comercial`
            WHEN 1 THEN 'Comercial'
            WHEN 2 THEN 'Exportacion'
        END) AS `comercial`,
        `base_empresa`.`codigo` AS `empresa`,
        `base_temporada`.`codigo` AS `temporada`,
        `base_zona`.`codigo` AS `zona`,
        (TO_DAYS(`prod_orden_despacho`.`fecha`) - TO_DAYS(`prod_existencia`.`fecha_packing`)) AS `dias_frio_packing`,
        `petiq`.`codigo_csg` AS `CSG_etiq`,
        (SELECT 
                GROUP_CONCAT(DISTINCT `cc_nota_venta`.`folio`
                        SEPARATOR ',')
            FROM
                (`prod_conf_orden_embarque_detalle`
                LEFT JOIN `cc_nota_venta` ON ((`cc_nota_venta`.`idnota_venta` = `prod_conf_orden_embarque_detalle`.`idnota_venta`)))
            WHERE
                (`prod_conf_orden_embarque_detalle`.`idembarque` = `oe`.`idorden_embarque`)) AS `nota_venta`,
        `prod_conf_predio`.`codigo_csg` AS `CSG_real`,
        `base_nave`.`fecha_zarpe` AS `fecha_zarpe`,
        `base_nave`.`fecha_arribo` AS `fecha_arribo`,
        (CASE `prod_existencia`.`atmosfera`
            WHEN 0 THEN 'No'
            WHEN 1 THEN 'Si'
            ELSE 'No Existe'
        END) AS `AC`,
        WEEK(`prod_orden_despacho`.`fecha`, 0) AS `semana`,
        DATE_FORMAT(`prod_orden_despacho`.`fecha`, '%m-%Y') AS `mes`,
        ROUND(`prod_conf_envase_operacional`.`peso_bruto`,
                2) AS `peso_bruto`,
        `prod_orden_despacho`.`sello` AS `sello_naviera`,
        (CASE `prod_existencia`.`contramuestra`
            WHEN 1 THEN 'MUE'
            ELSE (CASE `prod_existencia`.`comercial`
                WHEN 1 THEN 'C'
                ELSE 'E'
            END)
        END) AS `tipo_fruta`,
        `prod_conf_etiqueta`.`descripcion` AS `desc_etiqueta`,
        `prod_conf_envase_operacional`.`descripcion` AS `envase_operacional`,
        (SELECT 
                COUNT(DISTINCT `odd`.`folio`)
            FROM
                `prod_orden_despacho_detalle` `odd`
            WHERE
                ((`odd`.`activo` <> 0)
                    AND (`odd`.`idorden_despacho` = `prod_orden_despacho`.`idorden_despacho`)
                    AND (`prod_orden_despacho`.`activo` <> 0 ))) AS `cant_pallets`
    FROM
        ((((((((((((((((((((((((((((((((((((((((((`prod_orden_despacho`
        LEFT JOIN `prod_conf_orden_embarque` `oe` ON ((`oe`.`idorden_embarque` = `prod_orden_despacho`.`idorden_embarque`)))
        LEFT JOIN `prod_orden_despacho_detalle` ON ((`prod_orden_despacho_detalle`.`idorden_despacho` = `prod_orden_despacho`.`idorden_despacho`)))
        LEFT JOIN `base_nave` ON ((`base_nave`.`idnave` = `oe`.`idnave`)))
        LEFT JOIN `base_nombrenave` ON ((`base_nombrenave`.`idnombrenave` = `base_nave`.`idnombrenave`)))
        LEFT JOIN `prod_conf_tipo_nave` ON ((`prod_conf_tipo_nave`.`idtipo_nave` = `oe`.`tipo_nave`)))
        LEFT JOIN `base_naviera` ON ((`base_naviera`.`idnaviera` = `oe`.`idnaviera`)))
        LEFT JOIN `base_puerto` `puerto_origen` ON ((`puerto_origen`.`idpuerto` = `oe`.`idpto_embarque`)))
        LEFT JOIN `base_puerto` `puerto_destino` ON ((`puerto_destino`.`idpuerto` = `oe`.`idpto_destino`)))
        LEFT JOIN `base_pais` ON ((`base_pais`.`idpais` = `oe`.`idpais`)))
        LEFT JOIN `base_exportador` ON ((`base_exportador`.`idexportador` = `oe`.`exportador`)))
        LEFT JOIN `prod_conf_embarcador` ON ((`prod_conf_embarcador`.`idconf_embarcador` = `oe`.`embarcador`)))
        LEFT JOIN `prod_conf_agente_aduana` ON ((`prod_conf_agente_aduana`.`idconf_agente_aduana` = `oe`.`idagente_aduana`)))
        LEFT JOIN `base_contenedor` ON ((`base_contenedor`.`idcontenedor` = `prod_orden_despacho`.`idcontenedor`)))
        LEFT JOIN `base_recibidor` ON ((`base_recibidor`.`idrecibidor` = `oe`.`idrecibidor`)))
        LEFT JOIN `cc_transporte` ON ((`base_contenedor`.`idtransportista` = `cc_transporte`.`idtransporte`)))
        LEFT JOIN `cc_conf_empresa_transporte` ON ((`cc_conf_empresa_transporte`.`idconf_empresa_transporte` = `cc_transporte`.`idconf_empresa_transporte`)))
        LEFT JOIN `base_productor` ON ((`base_productor`.`idproductor` = `prod_orden_despacho_detalle`.`idproductor`)))
        LEFT JOIN `base_productor` `prod_etiquetado` ON ((`prod_etiquetado`.`idproductor` = `prod_orden_despacho_detalle`.`idproductor_etiquetado`)))
        LEFT JOIN `prod_conf_packing` ON ((`prod_conf_packing`.`idconf_packing` = `prod_orden_despacho_detalle`.`idconf_packing`)))
        LEFT JOIN `prod_conf_frio` ON ((`prod_conf_frio`.`idconf_frio` = `prod_orden_despacho_detalle`.`idconf_frio`)))
        LEFT JOIN `base_mercado` `mercado_uno` ON ((`mercado_uno`.`idmercado` = `prod_orden_despacho_detalle`.`idmercado_uno`)))
        LEFT JOIN `base_mercado` `mercado_dos` ON ((`mercado_dos`.`idmercado` = `prod_orden_despacho_detalle`.`idmercado_dos`)))
        LEFT JOIN `base_mercado` `mercado_tres` ON ((`mercado_tres`.`idmercado` = `prod_orden_despacho_detalle`.`idmercado_tres`)))
        LEFT JOIN `base_mercado` `mercado_cuatro` ON ((`mercado_cuatro`.`idmercado` = `prod_orden_despacho_detalle`.`idmercado_cuatro`)))
        LEFT JOIN `prod_existencia` ON ((`prod_orden_despacho_detalle`.`idexistencia` = `prod_existencia`.`idexistencia`)))
        LEFT JOIN `base_temporada` ON ((`base_temporada`.`idtemporada` = `prod_orden_despacho`.`idtemporada`)))
        LEFT JOIN `base_empresa` ON ((`base_empresa`.`idempresa` = `prod_orden_despacho`.`idempresa`)))
        LEFT JOIN `base_zona` ON ((`base_zona`.`idzona` = `prod_orden_despacho`.`idzona`)))
        LEFT JOIN `prod_conf_especie` ON ((`prod_conf_especie`.`idconf_especie` = `prod_existencia`.`idconf_especie`)))
        LEFT JOIN `prod_conf_envase_operacional` `envope_especie` ON ((`envope_especie`.`idconf_envase_operacional` = `prod_conf_especie`.`idconf_envase_operacional`)))
        LEFT JOIN `prod_conf_variedad` `vari` ON ((`vari`.`idconf_variedad` = `prod_existencia`.`idconf_variedad`)))
        LEFT JOIN `base_categoria` ON ((`base_categoria`.`idcategoria` = `prod_existencia`.`idcategoria`)))
        LEFT JOIN `prod_conf_calibre` ON ((`prod_conf_calibre`.`idconf_calibre` = `prod_existencia`.`idconf_calibre`)))
        LEFT JOIN `prod_conf_variedad` `varieti` ON ((`varieti`.`idconf_variedad` = `prod_existencia`.`idconf_variedad_etiquetada`)))
        LEFT JOIN `prod_conf_predio` ON ((`prod_conf_predio`.`idconf_predio` = `prod_existencia`.`idconf_predio`)))
        LEFT JOIN `prod_conf_predio` `petiq` ON ((`petiq`.`idconf_predio` = `prod_existencia`.`idconf_predio_etiquetado`)))
        LEFT JOIN `prod_conf_cuartel` ON ((`prod_conf_cuartel`.`idconf_cuartel` = `prod_existencia`.`idconf_cuartel`)))
        LEFT JOIN `prod_conf_etiqueta` ON ((`prod_conf_etiqueta`.`idconf_etiqueta` = `prod_existencia`.`idconf_etiqueta`)))
        LEFT JOIN `prod_conf_envase_operacional` ON ((`prod_conf_envase_operacional`.`idconf_envase_operacional` = `prod_existencia`.`idconf_envase_operacional`)))
        LEFT JOIN `prod_conf_plu` ON ((`prod_conf_plu`.`idconf_plu` = `prod_existencia`.`idconf_plu`)))
        LEFT JOIN `prod_conf_base_pallet` ON ((`prod_conf_base_pallet`.`idconf_base_pallet` = `prod_existencia`.`idconf_base_pallet`)))
        LEFT JOIN `prod_conf_tipo_tratamiento` ON ((`prod_conf_tipo_tratamiento`.`idconf_tipo_tratamiento` = `prod_existencia`.`idconf_tipo_tratamiento`)))
    WHERE
        ((`prod_orden_despacho`.`activo` <> 0)
            AND (`prod_orden_despacho`.`devolucion` = 0)
            AND (`prod_orden_despacho_detalle`.`activo` <> 0))) as t where booking='SNG9161885' """

table = "cc_v_despacho_odbc"

