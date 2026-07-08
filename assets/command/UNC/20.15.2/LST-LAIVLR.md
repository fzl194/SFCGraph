---
id: UNC@20.15.2@MMLCommand@LST LAIVLR
type: MMLCommand
name: LST LAIVLR（查询LAI与VLR号对应关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LAIVLR
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
- 电路域联合业务
- LAI与VLR号对应关系
status: active
---

# LST LAIVLR（查询LAI与VLR号对应关系）

## 功能

**适用网元：SGSN、MME**

该命令用于查看LAI与VLR的对应关系。

## 注意事项

- 该命令执行后立即生效。
- 不输入任何参数则表示查询所有信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BGNLAI | LAI | 可选必选说明：可选参数<br>参数说明：该参数用于指定待查询的位置区，由“MCC”、“MNC”和“LAC”组成。<br>数据来源：整网规划<br>取值范围：9~10位字符串<br>默认值：无<br>配置原则：<br>- “MCC”由3个阿拉伯数字组成，“MNC”由2到3个阿拉伯数字组成。<br>- LAC编码为16进制数，固定为4位，不足前面补0 |
| VLRNO | VLR号 | 可选必选说明：可选参数<br>参数说明：该参数用于表示位置区对应的VLR号码。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无<br>配置原则：一个VLR号可对应多个LAI区间。 |

## 操作的配置对象

- [LAI与VLR号对应关系（LAIVLR）](configobject/UNC/20.15.2/LAIVLR.md)

## 使用实例

1. 查看LAI为"308013101"的位置区对应的VLR号：
  LST LAIVLR: BGNLAI="308013101";
  ```
  %%LST LAIVLR: BGNLAI="308013101";%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
           LAI  =  308013101
      终止LAI   =  308013103
         VLR号  =  123456
  是否缺省VLR   =  是
  (结果个数 = 1)

  ---    END
  ```
2. 不输入任何参数，查看已经配置的所有LAI与VLR号的对应关系：
  LST LAIVLR:;
  ```
  %%LST LAIVLR:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   LAI        终止LAI    VLR号     是否缺省VLR

   308013101  308013103  123456    是         
   308013104  308015113  30801310  是         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LAI与VLR号对应关系(LST-LAIVLR)_72225095.md`
