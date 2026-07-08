---
id: UNC@20.15.2@MMLCommand@RMV SGSLKS
type: MMLCommand
name: RMV SGSLKS（删除SGs链路集）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGSLKS
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路集管理
status: active
---

# RMV SGSLKS（删除SGs链路集）

## 功能

![](删除SGs链路集(RMV SGSLKS)_26145436.assets/notice_3.0-zh-cn_2.png)

可能影响正在进行的业务。

**适用网元：MME**

此命令用于删除SGs链路集。删除时，需确认链路集没有被 [**ADD SGSLNK**](../SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) 所引用，否则链路集不能被删除。

## 注意事项

- 该命令执行后立即生效。
- 删除链路可能影响正在进行的业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：待删除链路集的索引。<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSLKS]] · SGs链路集（SGSLKS）

## 使用实例

删除 “链路集索引” 为 “0” 的链路集：

RMV SGSLKS: LSX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SGs链路集(RMV-SGSLKS)_26145436.md`
