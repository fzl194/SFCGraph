---
id: UNC@20.15.2@MMLCommand@DSP MTSMODEL
type: MMLCommand
name: DSP MTSMODEL（查询消息跟踪模型）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MTSMODEL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 消息跟踪
status: active
---

# DSP MTSMODEL（查询消息跟踪模型）

## 功能

该命令用于查询消息跟踪模型。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535<br>默认值：无。<br>配置原则：无。 |
| TRACETYPE | 跟踪类型 | 可选必选说明：可选参数。<br>参数含义：跟踪类型，由网元在适配包中定义。<br>取值范围：0~2147483647<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [消息跟踪模型（MTSMODEL）](configobject/UNC/20.15.2/MTSMODEL.md)

## 使用实例

1. 查询“网元ID”为“12”，“跟踪类型”为“17”的消息跟踪模型：
  ```
  %%DSP MTSMODEL: MEID=12, TRACETYPE=17;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
        网元ID  =  12
      跟踪类型  =  17
  拓展跟踪类型  =  17
  跟踪类型名称  =  E2E跟踪
  订阅服务名称  =  TestforCSPOMC|HttpDisCtrlService|UdmHttpService|UdmCcu
  (结果个数 = 1)

  ---    END
  ```
2. 查询“网元ID”为“12”，“跟踪类型”为“60102”的消息跟踪模型，跟踪类型“60102”配置了拓展跟踪类型：
  ```
  %%DSP MTSMODEL: MEID=12, TRACETYPE=60102;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  网元ID  跟踪类型  拓展跟踪类型  跟踪类型名称   订阅服务名称                                                   

  12      60102     10102         CSCF GTPC跟踪  cspjavacommonservicedemo                                       
  12      60102     60102         CSCF GTPC跟踪  TestforCSPOMC|CSPGoCommonServiceDemo
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询消息跟踪模型（DSP-MTSMODEL）_83186620.md`
