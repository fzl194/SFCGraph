---
id: UNC@20.15.2@MMLCommand@MOD TLSSCENE
type: MMLCommand
name: MOD TLSSCENE（修改TLS证书场景）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: TLSSCENE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS证书场景管理
status: active
---

# MOD TLSSCENE（修改TLS证书场景）

## 功能

该命令用于修改TLS证书场景配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定证书场景的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~254。<br>默认值：无<br>配置原则：无 |
| DESC | 证书使用场景描述 | 可选必选说明：可选参数<br>参数含义：描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TLSSCENE]] · TLS证书场景（TLSSCENE）

## 使用实例

若运营商想修改索引为1的TLS证书使用场景的描述，可以用如下命令：

```
MOD TLSSCENE: INDEX=1, DESC= "CA";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TLSSCENE.md`
