---
id: UNC@20.15.2@MMLCommand@RMV TLSPARA
type: MMLCommand
name: RMV TLSPARA（删除TLS参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TLSPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS安全管理
status: active
---

# RMV TLSPARA（删除TLS参数）

## 功能

该命令用于删除一组TLS参数。

## 注意事项

- 该命令执行后立即生效。

- 删除TLS参数后，如果该条配置关联的设备证书场景或CA证书场景没有被其他TLS参数配置关联，则需要通过[**RMV TLSSCENE**](../HTTP TLS证书场景管理/删除TLS证书场景（RMV TLSSCENE）_83813642.md)命令删除对应的TLS证书场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TLS参数索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>与<br>[**ADD HTTPLE**](../../HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)<br>中配置的TLS参数索引保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TLSPARA]] · TLS参数（TLSPARA）

## 使用实例

若运营商想删除索引为1的TLS配置，可以用如下命令：

```
RMV TLSPARA: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TLSPARA.md`
