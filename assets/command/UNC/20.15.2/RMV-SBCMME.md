---
id: UNC@20.15.2@MMLCommand@RMV SBCMME
type: MMLCommand
name: RMV SBCMME（删除SBC MME实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SBCMME
command_category: 配置类
applicable_nf:
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBC MME配置
status: active
---

# RMV SBCMME（删除SBC MME实体）

## 功能

**适用网元：CBCF**

此命令用于删除SBC MME实体配置。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令前，需要提前在UNC MML窗口上执行命令[**RMV SBCAPLNK**](../SBc链路/删除SBc链路(RMV SBCAPLNK)_26146374.md)，删除SBc链路中引用此SBC MME的链路。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEIDX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的MME的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>说明：可以通过<br>[**LST SBCMME**](查询SBC MME实体(LST SBCMME)_12436342.md)<br>命令查看已有配置，确认所要删除的MME的索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBCMME]] · SBC MME实体（SBCMME）

## 使用实例

删除一个索引为0的SBC MME配置:

```
RMV SBCMME: MMEIDX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SBC-MME实体(RMV-SBCMME)_47994769.md`
