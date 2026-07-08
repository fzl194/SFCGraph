---
id: UNC@20.15.2@MMLCommand@RMV VLROPC
type: MMLCommand
name: RMV VLROPC（删除VLR信令点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VLROPC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- VLR管理
status: active
---

# RMV VLROPC（删除VLR信令点）

## 功能

**适用NF：SMSF**

该命令用于删除VLR本局信令点指定配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | VLR信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VLR本局信令点索引。<br>数据来源：本端规划<br>取值范围：0~1<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROPC]] · VLR信令点（VLROPC）

## 使用实例

删除VLR信令点索引为1的VLROPC信令点。

```
RMV VLROPC: OPX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除VLR信令点(RMV-VLROPC)_46075484.md`
