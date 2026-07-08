# 调测QoS简单流分类 （VNRS_VNFC）

- [操作场景](#ZH-CN_OPI_0213119473__1.3.1)
- [必备事项](#ZH-CN_OPI_0213119473__1.3.2)
- [操作流程](#ZH-CN_OPI_0213119473__1.3.3)
- [操作步骤](#ZH-CN_OPI_0213119473__1.3.4)

## [操作场景](#ZH-CN_OPI_0213119473)

用于QoS简单流分类功能是否正常运行。

## [必备事项](#ZH-CN_OPI_0213119473)

前提条件

- 操作人员已经登录网络管理系统NMS（Network Management System）。
- 硬件安装已经完成。

数据

无

## [操作流程](#ZH-CN_OPI_0213119473)

调测QoS简单流分类特性操作流程如 [图1](#ZH-CN_OPI_0213119473__zh-cn_opi_0134584212_fig_dc_fenix_nps_mml_cfg_qos_000201) 所示。

**图1** 调测QoS简单流分类特性操作流程

<br>

![](调测QoS简单流分类（VNRS_VNFC）_13119473.assets/zh-cn_image_0000001564878336.png)

## [操作步骤](#ZH-CN_OPI_0213119473)

1. VNF1执行ping设置报文dscp值（0～63）。
    - **预期结果：**在VNF2上收到的ping报文，dscp值为0，调测结束。
    - **异常结果：** VNF2上收到的ping报文，dscp值不为0，请执行步骤2。
2. 查询DiffServ域是否与配置一致
  在 “MML命令行-UDG” 窗口上执行：
  [**LST QOSDIFFERSERV**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DS域配置/查询DS域（LST QOSDIFFERSERV）_49962062.md) : DSNAME="DS名称";
  **预期结果：** 查询结果与配置结果一致。
  ```
  LST QOSDIFFERSERV:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  DS域名 = ds1
  (结果个数 = 1)
  ---    END
  ```
3. 查询DiffServ域对应的QOSBA、QOSPHB配置及在接口上绑定QOSIFTRUST。
  在 “MML命令行-UDG” 窗口上执行：
  [**LST QOSBA**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/BA映射关系/查询QoS BA（LST QOSBA）_00441337.md) : DSNAME="ds1", BATYPE=ip_dscp;
    - **预期结果：**显示DiffServ域对应的QOSBA。
      ```
      RETCODE = 0  操作成功

      结果如下
      -------------------------
        DS域名 = ds1                                  
        Ba类型 = ip_dscp
          Ba值 = 0     
      服务分类 = be           
      颜色分类 = 绿
      (结果个数 = 1)
      ---    END
      ```
    - **异常结果：**查询不到DiffServ域对应的QOSBA，请重新配置。
  [**LST QOSPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/PHB映射关系/查询QoS PHB（LST QOSPHB）_00866029.md) : DSNAME="ds1", PHBTYPE=ip_dscp;
    - **预期结果：**显示DiffServ域对应的QOSPHB。
      ```
      RETCODE = 0  操作成功

      结果如下
      -------------------------
        DS域名 = ds1
       Phb类型 = ip_dscp
         Phb值 = 1
      服务分类 = be
      颜色分类 = 绿
       (结果个数 = 1)
      ---    END
      ```
    - **异常结果：**查询不到DiffServ域对应的QOSPHB，请重新配置。
  [**LST QOSIFTRUST**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/接口信任信息/查询QoS接口信任（LST QOSIFTRUST）_50280970.md) :;
    - **预期结果：**显示在以太主接口或者以太子接口上绑定的简单流分类。
      ```
      LST QOSIFTRUST: IFNAME="Ethernet
      64/0/3
      ";
      RETCODE = 0 操作成功

      结果如下
      -------------------------
           DS域名 = ds1
         接口名称 = Ethernet
      64/0/3

       8021p 标志 = 否
      (结果个数 = 1)
      --- END
      ```
    - **异常结果：**查询不到在以太主接口或者以太子接口上绑定的简单流分类，请重新配置。
4. 查询重定向至指定VPN的配置。
  在 “MML命令行-UDG” 窗口上执行：
  [**LST QOSRDRVPN**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/重定向VPN/查询QoS重定向VPN（LST QOSRDRVPN）_49961018.md) :；
    - **预期结果：**显示重定向至指定VPN的配置。
      ```
      RETCODE = 0  操作成功

      结果如下
      -------------------------
         接口名称  =  Ethernet
      64/0/3

          VPN名称  =  vpn1
      (结果个数 = 1)
      ---    END
      ```
    - **异常结果：**查询不到重定向至指定VPN的配置，请重新配置。
5. 查询以太接口QoS不检查PHB表。
  在 “MML命令行-UDG” 窗口上执行：
  [**LST QOSIFPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/QoS IF PHB/查询禁止QoS优先级映射的类型（LST QOSIFPHB）_00841321.md) : IFNAME="接口名称", PHBTYPE=出接口报文的优先级字段映射类型;
    - **预期结果：**显示以太接口Ethernet64/0/3QoS不检查PHB表。
      ```
      LST QOSIFPHB: IFNAME="Ethernet
      64/0/3
      ";
      RETCODE = 0 操作成功

      结果如下
      -------------------------
                            接口名称 = Ethernet
      64/0/3

      出接口报文的优先级字段映射类型 = IP报文的DSCP
      (结果数 = 1)
      --- 结束
      ```
    - **异常结果：**查询不到以太接口QoS不检查PHB表，请重新配置。
