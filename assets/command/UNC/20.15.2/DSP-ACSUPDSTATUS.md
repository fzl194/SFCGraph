---
id: UNC@20.15.2@MMLCommand@DSP ACSUPDSTATUS
type: MMLCommand
name: DSP ACSUPDSTATUS（显示升级状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ACSUPDSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# DSP ACSUPDSTATUS（显示升级状态）

## 功能

该命令用于显示RU升级状态。

本命令只适用于ACS服务，其他微服务请使用DSP UPDSTATUS命令。

## 注意事项

RU状态是offline且后台进程正常时，RU升级状态查询结果不是Null。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：1-63位字符串，区分大小写，不支持空格。<br>默认值：无 |
| STATUS | 状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示升级状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- On：开始升级。<br>- Off：结束升级。<br>- Null: 单板状态未知。<br>默认值：无 |

## 操作的配置对象

- [升级状态（ACSUPDSTATUS）](configobject/UNC/20.15.2/ACSUPDSTATUS.md)

## 使用实例

显示RU升级状态：

```
DSP ACSUPDSTATUS:;
```

```
RETCODE = 0  操作成功 

结果如下:  
-------------------------  
RU名称                     状态
ACS_OM_RU_0002             升级结束
ACS_OM_RU_0001             升级结束
(结果个数 = 2)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示升级状态（DSP-ACSUPDSTATUS）_89080530.md`
