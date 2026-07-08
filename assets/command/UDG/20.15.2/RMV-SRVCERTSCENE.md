---
id: UDG@20.15.2@MMLCommand@RMV SRVCERTSCENE
type: MMLCommand
name: RMV SRVCERTSCENE（删除配置证书场景）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SRVCERTSCENE
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继证书场景
status: active
---

# RMV SRVCERTSCENE（删除配置证书场景）

## 功能

**适用NF：UPF、PGW-U**

该命令用于删除配置证书场景。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 证书使用场景名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定证书使用场景的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。区分大小写，不允许仅大小写不同的重复记录。不支持中文字符，只能由“_”、数字和大小写字母组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SRVCERTSCENE]] · 配置证书场景（SRVCERTSCENE）

## 使用实例

删除配置证书场景：

```
RMV SRVCERTSCENE: SCENE="test01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SRVCERTSCENE.md`
