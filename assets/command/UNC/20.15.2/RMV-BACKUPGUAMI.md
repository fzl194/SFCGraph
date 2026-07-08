---
id: UNC@20.15.2@MMLCommand@RMV BACKUPGUAMI
type: MMLCommand
name: RMV BACKUPGUAMI（删除供备GUAMI信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BACKUPGUAMI
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- 备用GUAMI列表管理
status: active
---

# RMV BACKUPGUAMI（删除供备GUAMI信息）

## 功能

**适用NF：AMF**

该命令用于删除将本AMF用作备用AMF的某个GUAMI信息。

## 注意事项

- 该命令执行后立即生效。

- 增加、删除或者修改本AMF提供备用功能的GUAMI信息，都会引起本AMF到NRF的注册更新。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | GUAMI索引 | 可选必选说明：必选参数<br>参数含义：该参数是将本AMF作为备用AMF的GUAMI的配置记录索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [供备GUAMI信息（BACKUPGUAMI）](configobject/UNC/20.15.2/BACKUPGUAMI.md)

## 使用实例

Pool内其它AMF的某个GUAMI将本AMF用作备用节点，当该AMF从Pool内迁出时，本AMF的供备GUAMI列表需要同步刷新，执行如下命令：

```
RMV BACKUPGUAMI: INDEX=11;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除供备GUAMI信息（RMV-BACKUPGUAMI）_09653060.md`
