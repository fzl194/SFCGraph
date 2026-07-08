---
id: UNC@20.15.2@MMLCommand@LST SAIGEO
type: MMLCommand
name: LST SAIGEO（查询服务区标识与地理坐标对照关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SAIGEO
command_category: 查询类
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
- SAI和地理坐标对照表
status: active
---

# LST SAIGEO（查询服务区标识与地理坐标对照关系）

## 功能

**适用网元：SGSN**

此命令用于查询服务区标识SAI与地理位置经纬度坐标的对应关系。SGSN利用这个对应关系完成SAI与地理位置经纬度坐标之间的转换，提供给LCS MT/NI/MO流程使用。不输入参数时将显示本SGSN下配置的所有服务区标识SAI与地理位置经纬度坐标的对应关系。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SAI | 服务区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务区标识。服务区由一个或多个小区构成。服务区标识由位置区标识LAI(Location Area Identification)和服务区码SAC(ServIce Area Code)组成。位置区标识由移动国家码MCC(Mobile Country Code)、移动网络码MNC(Mobile Network Code)和位置区码LAC(Location Area Code)组成。移动国家码MCC由3位数字组成，移动网络码MNC由2～3位数字组成，位置区码是在GSM PLMN中标识一个位置区的4位十六进制数。服务区码是在一个位置区中标识一个服务区的4位十六进制数。<br>取值范围：13～14位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SAIGEO]] · 服务区标识与地理坐标对照关系（SAIGEO）

## 使用实例

列出所有SAI与地理位置经纬度坐标的对应关系：

LST SAIGEO:;

```
%%LST SAIGEO:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
    服务区标识  =  1230907551234(123-09-0755-1234)
      纬度类型  =  北纬
      纬度(度)  =  5
      纬度(分)  =  15
      纬度(秒)  =  25
      经度类型  =  西经
      经度(度)  =  35
      经度(分)  =  45
      经度(秒)  =  55
服务区半径(米)  =  35000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务区标识与地理坐标对照关系(LST-SAIGEO)_26305602.md`
