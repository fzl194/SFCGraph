---
id: UNC@20.15.2@MMLCommand@RMV RESELECTUPCAUSE
type: MMLCommand
name: RMV RESELECTUPCAUSE（删除重选UPF故障原因值）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESELECTUPCAUSE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 故障原因值重选UPF
status: active
---

# RMV RESELECTUPCAUSE（删除重选UPF故障原因值）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除重选UPF的故障原因值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FAULTCAUSE | 故障原因值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF重选的故障原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESELECTUPCAUSE]] · 重选UPF故障原因值（RESELECTUPCAUSE）

## 使用实例

删除重选UPF故障原因值75。

```
RMV RESELECTUPCAUSE: FAULTCAUSE =75;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RESELECTUPCAUSE.md`
