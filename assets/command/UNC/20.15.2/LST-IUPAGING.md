---
id: UNC@20.15.2@MMLCommand@LST IUPAGING
type: MMLCommand
name: LST IUPAGING（查询Iu接口寻呼数据）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUPAGING
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu接口寻呼数据
status: active
---

# LST IUPAGING（查询Iu接口寻呼数据）

## 功能

**适用网元：SGSN**

该命令用于查询3G寻呼信息，在触发3G寻呼时，利用此信息根据RAI定位RNC。系统根据MS原来的路由区是否在3G寻呼表（2G寻呼表）内存在来判定ATTACH、RAU、RELOCATION等流程是Inter-SGSN还是Intra-SGSN。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | 位置区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本SGSN管辖位置区的标识。<br>取值范围：9~10位字符串<br>默认值：无<br>说明：LAI = MCC + MNC + LAC。MCC由3个阿拉伯数字组成，MNC由2到3个阿拉伯数字组成，LAC是十六进制数，占2个字节。 |
| RAC | 路由区编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本SGSN管辖路由区的编码。<br>取值范围：0x00~0xFF<br>默认值：无<br>说明：RAC是十六进制数，占1个字节。 |
| RNCINDEX | RNC索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RNC索引，可查询RNC信息表获得。<br>取值范围：0~511<br>默认值：无 |

## 操作的配置对象

- [Iu接口寻呼数据（IUPAGING）](configobject/UNC/20.15.2/IUPAGING.md)

## 使用实例

查询3G寻呼表所有记录:

LST IUPAGING:;

```
%%LST IUPAGING:;%%
RETCODE = 0  操作成功。

3G寻呼配置表
------------
位置区标识   路由区编码   RNC索引
            
123070001    0x01         1
123070001    0x02         1
123070102    0x01         11
123070102    0x02         11
123072504    0x00         1
123072520    0x01         6
(结果个数 = 6)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Iu接口寻呼数据(LST-IUPAGING)_26146036.md`
