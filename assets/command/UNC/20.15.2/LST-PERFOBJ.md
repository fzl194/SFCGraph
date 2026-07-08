---
id: UNC@20.15.2@MMLCommand@LST PERFOBJ
type: MMLCommand
name: LST PERFOBJ（查询性能对象信息）
nf: UNC
version: 20.15.2
verb: LST
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

# LST PERFOBJ（查询性能对象信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询性能统计对象信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：待查询的测量对象类型。<br>取值范围：<br>- “APN(APN)”<br>- “TAIGP(TAI组)”<br>- “HSSHOSTNAME(HSS主机名)”<br>默认值：无<br>说明：选择<br>“APN(APN)”<br>，表示查询所有APN记录；选择<br>“TAIGP(TAI组)”<br>，表示查询所有TAI组记录；选择<br>“HSSHOSTNAME(HSS主机名)”<br>，表示查询所有HSS主机名记录。 |
| NAME | 对象名称 | 可选必选说明：条件可选参数<br>参数含义：待查询的APN测量对象的名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“APN(APN)”<br>后生效。<br>取值范围：0~63位字符串<br>默认值：无<br>说明：输入参数<br>“NAME”<br>，表示查询指定记录。 |
| INDEX | 索引 | 可选必选说明：条件可选参数<br>参数含义：待查询的APN测量对象索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“APN(APN)”<br>后生效。<br>取值范围：1~1000<br>默认值：无<br>说明：输入参数<br>“INDEX”<br>，表示查询指定记录。 |
| APNTYPE | APN类型 | 可选必选说明：条件可选参数<br>参数含义：待查询的APN测量对象的类型。APN有两种类型：自动配置APN，手动配置APN。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“APN(APN)”<br>后生效。<br>取值范围：<br>- “MANUAPN(手动配置APN)”<br>- “AUTOAPN(自动配置APN)”<br>默认值：无<br>说明：输入参数<br>“APNTYPE”<br>，表示查询指定记录。 |
| TAIGPN | TAI组名 | 可选必选说明：条件可选参数<br>参数含义：待查询的TAI组测量对象的名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>后生效。<br>取值范围：0~32位字符串<br>默认值：无<br>说明：输入参数<br>“TAIGPN”<br>，表示查询指定记录。 |
| TAIGPTYPE | TAI组类型 | 可选必选说明：条件可选参数<br>参数含义：待查询的TAI组测量对象的类型。TAI组有两种类型：自动统计TAI，系统缺省为每个TAI创建一个TAI组，TAI组名即为TAI值；手动配置TAI组，为可以手动创建TAI组，将多个TAI合并到一个TAI组中，进行性能统计。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>后生效。<br>取值范围：<br>- “MANUTAIG(手动配置TAI组)”<br>- “AUTOTAIG(自动配置TAI组)”<br>默认值：无<br>说明：输入参数<br>“TAIGPTYPE”<br>，表示查询指定记录。 |
| HSSNAME | HSS对象名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的HSS对象名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“HSSHOSTNAME(HSS主机名)”<br>后生效。<br>取值范围：0~32位字符串<br>默认值：无 |
| HSSNAMEINDEX | HSS对象名称索引 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的HSS对象名称索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“HSSHOSTNAME(HSS主机名)”<br>后生效。<br>取值范围：1~64<br>默认值：无 |

## 操作的配置对象

- [性能对象信息（PERFOBJ）](configobject/UNC/20.15.2/PERFOBJ.md)

## 使用实例

- 查询系统配置的所有APN信息：
  LST PERFOBJ: MOC=APN;
  ```
     
  %%LST PERFOBJ: MOC=APN;%%
  RETCODE = 0  操作成功。

  查询对象名称与索引对应关系
  --------------------------
  测量对象类型  对象名称         索引   APN类型

  APN           HUAWEI.COM        1     手动配置APN
  APN           HUAWEITEST.COM    2     手动配置APN
  (结果个数 = 2)

  ---    END
  ```
- 查询系统配置的所有TAI组信息
  LST PERFOBJ: MOC=TAIGP;
  ```
     
  %%LST PERFOBJ: MOC=TAIGP;%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------
  测量对象类型    TAI组名      TAI组类型       TAI组索引

  TAIGP           huawei       手动配置TAI组   1
  TAIGP           huaweitest   手动配置TAI组   2
  (结果个数 = 2)

  ---    END
  ```
- 查询系统配置的所有HSS对象信息
  LST PERFOBJ: MOC=HSSHOSTNAME;
  ```
  %%LST PERFOBJ: MOC=HSSHOSTNAME;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
       测量对象类型  =  HSS主机名
        HSS对象名称  =  LOCAL
    HSS对象名称索引  =  1
  HSS主机名匹配规则  =  *.EPC.MNC123.MCC456.3GPPNETWORK.ORG
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询性能对象信息(LST-PERFOBJ)_26306000.md`
