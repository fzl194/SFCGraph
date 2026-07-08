---
id: UDG@20.15.2@MMLCommand@LST SDRPARAMS
type: MMLCommand
name: LST SDRPARAMS（查询SDR参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SDRPARAMS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- TCP开关控制
status: active
---

# LST SDRPARAMS（查询SDR参数）

## 功能

该命令用于查询SDR服务的相关参数。SDR主要功能是为微服务间提供分布式透明通信。

> **说明**
> - SDR参数ID为0的功能该版本不支持；
> - SDR参数ID为4的功能，其对应的PARAVALUE1表示Fabric平面可靠传输的校验和开关。修改PARAVALUE1的值后，请全量复位POD，否则会上报系统命令配置修改未生效告警。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAID | 参数ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定SDR命令标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~10。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRPARAMS]] · SDR参数（SDRPARAMS）

## 使用实例

查询SDR参数：

```
%%LST SDRPARAMS: PARAID=1;%%
RETCODE = 0  操作成功

结果如下
--------
      参数ID  =  1
第一个参数值  =  0
第二个参数值  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SDRPARAMS.md`
