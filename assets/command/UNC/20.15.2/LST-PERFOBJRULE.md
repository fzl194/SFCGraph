---
id: UNC@20.15.2@MMLCommand@LST PERFOBJRULE
type: MMLCommand
name: LST PERFOBJRULE（查询性能对象规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFOBJRULE
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
- 性能对象规则管理
status: active
---

# LST PERFOBJRULE（查询性能对象规则）

## 功能

**适用网元：SGSN、MME**

该命令用于查询指定性能统计对象的统计规则。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：待查询规则的测量统计对象类型。<br>取值范围：<br>- “TAIGP(TAI组)”<br>默认值：无<br>说明：仅输入<br>“TAIGP(TAI组)”<br>，表示查询所有TAI组记录。 |
| TAIGPN | TAI组名 | 可选必选说明：条件可选参数<br>参数含义：待查询TAI组规则的TAI组名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>后生效。<br>取值范围：1~32位字符串<br>默认值：无<br>说明：输入参数<br>“TAIGPN”<br>，表示查询指定记录。 |
| TAI | TAI | 可选必选说明：条件可选参数<br>参数含义：待查询的TAI。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>后生效。<br>取值范围：9~10位字符串<br>默认值：无<br>说明：- TAI由MCC、MNC和TAC组成。MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，固定为4位，不足前面补0。<br>- 输入参数“TAI”，表示查询指定记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFOBJRULE]] · 性能对象规则（PERFOBJRULE）

## 使用实例

查询系统配置的所有TAI组规则信息：

LST PERFOBJRULE: MOC=TAIGP;

```
     
%%LST PERFOBJRULE: MOC=TAIGP;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
 测量对象类型   TAI组名   TAI组规则索引  起始TAI     终止TAI  

 TAI组          huawei    1              308014101   308014103
 TAI组          huawei    2              308014111   308014111
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFOBJRULE.md`
