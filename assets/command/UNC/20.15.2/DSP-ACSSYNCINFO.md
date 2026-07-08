---
id: UNC@20.15.2@MMLCommand@DSP ACSSYNCINFO
type: MMLCommand
name: DSP ACSSYNCINFO（查询ACS的配置同步信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ACSSYNCINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 对账管理
status: active
---

# DSP ACSSYNCINFO（查询ACS的配置同步信息）

## 功能

该命令用于查询ACS服务向其他微服务配置同步的结果。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选。<br>参数含义：用于指定需要查询配置同步结果的微服务名称，若不输入，则表示查询所有微服务。<br>取值范围：长度范围1~256的字符串。<br>默认值：无。 |
| INSTANCEID | 实例ID | 可选必选说明：可选。<br>参数含义：用于指定需要查询配置同步结果的微服务实例ID，若不输入，则表示查询所有服务实例。<br>取值范围：长度范围1~256的字符串。<br>默认值：无。 |
| STATE | 同步状态 | 可选必选说明：可选。<br>参数含义：用于指定需要查询配置同步结果的微服务同步状态，若不输入，则表示查询所有同步状态。<br>取值范围：枚举类型。<br>- success(同步成功)：查询配置同步状态为同步成功的微服务。<br>- failed(同步失败)：查询配置同步状态为同步失败的微服务。<br>- never(从未同步过)：查询未进行过配置同步的微服务。<br>- syncing(正在同步)：查询正在进行配置同步的微服务。<br>- 默认值：无。 |

## 操作的配置对象

- [ACS的配置同步信息（ACSSYNCINFO）](configobject/UNC/20.15.2/ACSSYNCINFO.md)

## 使用实例

```
%%DSP ACSSYNCINFO: SERVICENAME="DemoGoServer", INSTANCEID="2716960338878364264", STATE=success;%%
RETCODE = 0  操作成功

操作结果如下
------------
          服务名称  =  DemoGoServer
            实例ID  =  3537176978061755714
    远端设备IP地址  =  10.20.20.20
  远端设备IP端口号  =  40051
          同步状态  =  同步成功
上一次同步结束时间  =  2021-03-12, 20:09:58:601+08:00
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ACS的配置同步信息(DSP-ACSSYNCINFO)_87082450.md`
