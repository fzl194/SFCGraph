---
id: UNC@20.15.2@MMLCommand@SET CDRSTRGSTATUS
type: MMLCommand
name: SET CDRSTRGSTATUS（设置话单缓存目录状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CDRSTRGSTATUS
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费缓存
- 缓存目录
status: active
---

# SET CDRSTRGSTATUS（设置话单缓存目录状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置话单缓存目录状态。对话单缓存目录charge1或者charge2中的话单文件进行操作之前，必须在锁定该目录之后才可进行。操作完毕后，要将缓存目录charge1或者charge2解锁。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2048。
- 话单缓存目录charge1和charge2不能同时被锁定。
- POD缓存路径被锁定时不允许缩容。
- POD缓存路径解锁动作处理完前不允许缩容。
- 使用该命令锁定话单缓存目录之后，如果遇到话单缓存周期扫描，会导致告警清除，需要确认影响后使用该功能。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| DIRECTORY | 话单缓存目录 | 可选必选说明：必选参数<br>参数含义：该参数用于指定话单缓存目录。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CHARGE1：主话单缓存目录。<br>- CHARGE2：备话单缓存目录。<br>- CONVERGED1：融合计费的主话单缓存目录。<br>- CONVERGED2：融合计费的备话单缓存目录。<br>默认值：无<br>配置原则：无 |
| STATUS | 目录状态 | 可选必选说明：必选参数<br>参数含义：该参数用于显示话单缓存目录状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UNLOCK：解锁目录。<br>- LOCK：锁定目录。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [话单缓存目录状态（CDRSTRGSTATUS）](configobject/UNC/20.15.2/CDRSTRGSTATUS.md)

## 使用实例

当对PODNAME为uncpod-011-30-0-217的主话单缓存目录charge1进行操作之前，必须使用该命令将POD为uncpod-011-30-0-217的主话单缓存目录加锁：

```
SET CDRSTRGSTATUS:PODNAME="uncpod-011-30-0-217",DIRECTORY=CHARGE1,STATUS=LOCK;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置话单缓存目录状态（SET-CDRSTRGSTATUS）_09897006.md`
