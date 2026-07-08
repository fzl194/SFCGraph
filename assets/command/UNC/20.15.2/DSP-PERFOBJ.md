---
id: UNC@20.15.2@MMLCommand@DSP PERFOBJ
type: MMLCommand
name: DSP PERFOBJ（显示性能对象信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PERFOBJ
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象管理
status: active
---

# DSP PERFOBJ（显示性能对象信息）

## 功能

**适用网元：SGSN、MME**

本命令用于显示特定的TAI组下包含的TAI详细列表。

## 注意事项

无。

## 权限

manage-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：待查询的测量对象类型。<br>取值范围：<br>- “TAIGP(TAI组)”<br>默认值：无 |
| TAIGPN | TAI组名 | 可选必选说明：条件必选参数<br>参数含义：待查询的TAI组测量对象的名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>后生效。<br>取值范围：1~32位字符串<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFOBJ]] · 性能对象信息（PERFOBJ）

## 使用实例

查询系统配置的TAI组“huawei”所包含的TAI详细列表：

DSP PERFOBJ: MOC=TAIGP, TAIGPN="huawei", SERVICETYPE="USN_VNFC";

```
%%DSP PERFOBJ: MOC=TAIGP, TAIGPN="huawei", 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下:
-------------------------
TAI组规则索引	TAI       	

1             308014101	
2             308014111	

(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PERFOBJ.md`
