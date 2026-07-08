---
id: UDG@20.15.2@MMLCommand@RMV SLICEINSTINFO
type: MMLCommand
name: RMV SLICEINSTINFO（删除切片实例信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SLICEINSTINFO
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片实例信息
status: active
---

# RMV SLICEINSTINFO（删除切片实例信息）

## 功能

**适用NF：UPF**

此命令用于删除切片实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSIINFO | NsiInfo | 可选必选说明：必选参数<br>参数含义：NSIINFO。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无<br>配置原则：无 |
| NSSIID | NSSI ID | 可选必选说明：必选参数<br>参数含义：NSSI ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SLICEINSTINFO]] · 切片实例信息（SLICEINSTINFO）

## 使用实例

删除切片实例信息：

```
RMV SLICEINSTINFO: NSSIID="1", NsiInfo="test";
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除切片实例信息（RMV-SLICEINSTINFO）_51061263.md`
