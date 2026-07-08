---
id: UNC@20.15.2@MMLCommand@LST CELLGEO
type: MMLCommand
name: LST CELLGEO（查询CELLID与地理坐标对应关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CELLGEO
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
- 小区地理信息
status: active
---

# LST CELLGEO（查询CELLID与地理坐标对应关系）

## 功能

**适用网元：SGSN**

此命令用于查询小区标识CID与地理位置经纬度坐标的对应关系。SGSN利用这个对应关系完成CID与地理位置经纬度坐标之间的转换，提供给LCS MT/NI流程使用。不输入参数时将显示本SGSN下配置的所有小区标识CID与地理位置经纬度坐标的对应关系。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CID | 小区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定小区的标识，CID = MCC + MNC + LAC + RAC + CI。<br>取值范围：15~16位十六进制数<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CELLGEO]] · CELLID与地理坐标对应关系（CELLGEO）

## 使用实例

列出所有CID与地理位置经纬度坐标的对应关系：

LST CELLGEO:;

```
%%LST CELLGEO:;%%
RETCODE = 0  操作成功。

查询结果如下
------------
     小区标识  =  123178880300000(123-17-34944-48-0)
     纬度类型  =  北纬
   纬度（度）  =  32
   纬度（分）  =  6
   纬度（秒）  =  6
     经度类型  =  西经
   经度（度）  =  62
   经度（分）  =  7
   经度（秒）  =  6
小区半径（m）  =  62
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CELLID与地理坐标对应关系(LST-CELLGEO)_72225469.md`
