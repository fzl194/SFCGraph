---
id: UDG@20.15.2@MMLCommand@RMV INSAPROTPARA
type: MMLCommand
name: RMV INSAPROTPARA（删除单协议推理配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: INSAPROTPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 基于协议的识别功能配置
status: active
---

# RMV INSAPROTPARA（删除单协议推理配置）

## 功能

**适用NF：PGW-U、UPF**

删除单协议推理配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示协议组包含的协议的名字。<br>数据来源：本端规划<br>取值范围：1、字符串类型，输入长度范围为1～31; 2、不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置协议前需使用工程命令smctrldsp protocol-list sub-protocol查询三级协议表；使用MML命令DSP CFGTABLEDATA: OMUTYPE=master, DBTYPE=running, QUERYTYPE=table-data, TABLENAME="AISAppProtocol", SERVICEINSTANCE="ACS";查询INSA自定义协议表。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@INSAPROTPARA]] · 单协议推理配置（INSAPROTPARA）

## 使用实例

删除http协议的单条协议推理参数设置：

```
RMV INSAPROTPARA:PROTOCOLNAME="http";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-INSAPROTPARA.md`
