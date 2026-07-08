---
id: UNC@20.15.2@MMLCommand@RMV CELLGEO
type: MMLCommand
name: RMV CELLGEO（删除CELLID与地理坐标对应关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CELLGEO
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- 小区地理信息
status: active
---

# RMV CELLGEO（删除CELLID与地理坐标对应关系）

## 功能

**适用网元：SGSN**

此命令用于删除小区标识CID与地理位置经纬度坐标的对应关系。

## 注意事项

- 此命令执行后立即生效。
- 小区标识CID必须在CID与地理坐标对照表中存在。
- 删除小区标识CID与地理位置经纬度坐标的对应关系后，在对该小区下2G附着的用户的定位流程中，定位流程会失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CID | 小区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定小区的标识，CID = MCC + MNC + LAC + RAC + CI。<br>取值范围：15~16位十六进制数<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CELLGEO]] · CELLID与地理坐标对应关系（CELLGEO）

## 使用实例

将CID为0123456789012345与地理位置经纬度坐标的对应关系删除：

RMV CELLGEO: CID="0123456789012345";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除CELLID与地理坐标对应关系(RMV-CELLGEO)_72345389.md`
