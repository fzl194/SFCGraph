---
id: UNC@20.15.2@MMLCommand@ADD DSCPMAP
type: MMLCommand
name: ADD DSCPMAP（添加DSCP值到VLAN优先级的映射）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DSCPMAP
command_category: 配置类
effect_mode: ''
is_dangerous: false
max_records: 63
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- DSCP映射VLAN优先级
status: active
---

# ADD DSCPMAP（添加DSCP值到VLAN优先级的映射）

## 功能

该命令用于添加DSCP值到VLAN优先级的映射。

## 注意事项

- 该命令最大记录数为63。
- DSCP值到VLAN优先级的映射对跨IPU的内联口入报文不生效。
- DSCP值到VLAN优先级的映射对外联口入报文不生效。
- 如果报文出接口使能了简单流分类，则DSCP值到VLAN优先级的映射不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSCP | DSCP值 | 可选必选说明：必选参数<br>参数含义：该参数用来表示DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无 |
| TYPE | 优先级类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示优先级类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- 8021p：8021p优先级。<br>- exp：EXP优先级。<br>默认值：无 |
| VALUE | 优先级数值 | 可选必选说明：必选参数<br>参数含义：该参数用来表示优先级数值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～7。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DSCPMAP]] · DSCP值到VLAN优先级的映射（DSCPMAP）

## 使用实例

添加DSCP值到VLAN优先级的映射：

```
ADD DSCPMAP:DSCP=8,VALUE=4,TYPE=8021p;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DSCPMAP.md`
