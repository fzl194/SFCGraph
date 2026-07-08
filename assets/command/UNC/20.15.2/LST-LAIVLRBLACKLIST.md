---
id: UNC@20.15.2@MMLCommand@LST LAIVLRBLACKLIST
type: MMLCommand
name: LST LAIVLRBLACKLIST（查询LAIVLR黑名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LAIVLRBLACKLIST
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- LAIVLR黑名单管理
status: active
---

# LST LAIVLRBLACKLIST（查询LAIVLR黑名单）

## 功能

**适用网元：MME**

该命令用于查看LAI与VLR的黑名单对应关系。

## 注意事项

- 该命令执行后立即生效。
- 不输入任何参数则表示查询所有信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：可选参数<br>参数说明：该参数用于表示位置区对应的VLR号码。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无 |
| BGNLAI | 起始LAI | 可选必选说明：可选参数<br>参数说明：该参数是指对应一个VLR号的LAI黑名单的起始位置区。<br>数据来源：整网规划<br>取值范围：9~10位字符串<br>默认值：无 |

## 操作的配置对象

- [LAIVLR黑名单（LAIVLRBLACKLIST）](configobject/UNC/20.15.2/LAIVLRBLACKLIST.md)

## 使用实例

1. 1.查看LAI为"308013101"的位置区对应的VLR号的黑名单对应关系：
  LST LAIVLRBLACKLIST: BGNLAI="308013101";
  ```
  %%LST LAIVLRBLACKLIST: BGNLAI="308013101";%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
         VLR号  =  123456
       起始LAI  =  308013101
      终止LAI   =  308013103

  (结果个数 = 1)

  ---    END
  ```
2. 2.不输入任何参数，查看已经配置的所有LAI与VLR的黑名单对应关系：
  LST LAIVLRBLACKLIST:;
  ```
  %%LST LAIVLRBLACKLIST:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   VLR号    起始LAI    终止LAI    
 
   123456   308013101  308013103  
   30801310 308013104  308015113  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LAIVLR黑名单(LST-LAIVLRBLACKLIST)_26145424.md`
