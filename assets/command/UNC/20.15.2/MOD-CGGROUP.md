---
id: UNC@20.15.2@MMLCommand@MOD CGGROUP
type: MMLCommand
name: MOD CGGROUP（修改CG组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CGGROUP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- CG组
status: active
---

# MOD CGGROUP（修改CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来修改CG组的描述信息。

## 注意事项

- 该命令执行后立即生效。
- 输入空格则清除CG组描述。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGGRPID | CG组ID | 可选必选说明：必选参数<br>参数含义：CG组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | CG组描述 | 可选必选说明：可选参数<br>参数含义：CG组的描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGGROUP]] · CG组（CGGROUP）

## 使用实例

修改CG组ID为1的CG组的描述为"test"：

```
MOD CGGROUP: CGGRPID=1, DESCRIPTION="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CGGROUP.md`
