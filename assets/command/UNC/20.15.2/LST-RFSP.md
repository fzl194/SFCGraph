---
id: UNC@20.15.2@MMLCommand@LST RFSP
type: MMLCommand
name: LST RFSP（查询RFSP配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RFSP
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- RFSP管理
- RFSP策略管理
- RFSP参数配置
status: active
---

# LST RFSP（查询RFSP配置）

## 功能

**适用网元：SGSN、MME**

此命令用于查看RFSP ID的配置记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>该参数用于指定配置RFSP ID的用户范围。<br>取值范围：<br>- “ALL_IMSI(所有用户)”<br>- “SPECIAL_IMSI(指定用户)”<br>- “FOREIGN_USER（外网用户）”<br>- “HOME_USER（本网用户）”<br>默认值：无<br>说明：填入所要查找记录的用户范围，如不填入则查询所有记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户群的IMSI前缀。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“SPECIAL_IMSI(指定用户)”<br>后生效。<br>取值范围：5～15位数字<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：<br>该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RFSP]] · RFSP配置（RFSP）

## 使用实例

场景参见 [**ADD RFSP**](增加RFSP配置(ADD RFSP)_26305350.md) 的命令使用实例。

查询全部用户的RFSP ID记录：

LST RFSP:;

```
%%LST RFSP:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
 用户范围  IMSI前缀  运营商标识  RFSP来源  目标RFSP  使用扩展RFSP策略

 所有用户  NULL      NULL        配置优先  3         否              
 指定用户  30808     NULL        配置优先  1         否              
 外网用户  NULL      0           配置优先  2         否 
(结果个数 = 3)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RFSP.md`
