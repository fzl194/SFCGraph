---
id: UNC@20.15.2@MMLCommand@LST NRFNFINFOFMT
type: MMLCommand
name: LST NRFNFINFOFMT（查询NF私有信息格式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNFINFOFMT
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF私有信息格式管理
status: active
---

# LST NRFNFINFOFMT（查询NF私有信息格式）

## 功能

**适用NF：NRF**

该命令用于查询服务发现、检索响应及通知请求中NF的私有信息字段格式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示设置NF私有信息格式的目标网元类型。<br>数据来源：本端规划<br>取值范围：<br>- BSF（BSF）<br>默认值：无<br>配置原则：<br>当前只支持设置BSF的私有信息格式。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFNFINFOFMT]] · NF私有信息格式（NRFNFINFOFMT）

## 使用实例

查询BSF的私有信息格式。

```
LST NRFNFINFOFMT:;
%%LST NRFNFINFOFMT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
网元类型  =  BSF
NF私有信息格式  =  ARRAY
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFNFINFOFMT.md`
