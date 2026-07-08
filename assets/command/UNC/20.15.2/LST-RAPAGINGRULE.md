---
id: UNC@20.15.2@MMLCommand@LST RAPAGINGRULE
type: MMLCommand
name: LST RAPAGINGRULE（查询基于路由区的寻呼参数设置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RAPAGINGRULE
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于路由区的寻呼参数设置
status: active
---

# LST RAPAGINGRULE（查询基于路由区的寻呼参数设置）

## 功能

**适用网元：SGSN**

该命令用于查询基于路由区的2/3G寻呼参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家代码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区域码。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RAPAGINGRULE]] · 基于路由区的寻呼参数设置（RAPAGINGRULE）

## 使用实例

1. 不输入参数，查询所有添加的基于路由区的寻呼策略配置信息：
  LST RAPAGINGRULE:;
  ```
  %%LST RAPAGINGRULE:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   移动国家代码  移动网号  位置区域码  路由区域码  星期序号  起始时间  终止时间  T3313(s)  N3313(times)  重寻呼间隔递增值(s)  描述

   123           01        0x1001      0x01        星期一    16:14     17:14     6         2             0                    noname     
   123           01        0x1001      0x01        星期一    17:15     17:18     6         2             0                    noname     
  (结果个数 = 2)

  ---    END
  ```
2. 输入RAI(MCC+MNC+LAC+RAC)参数，查询指定路由区的寻呼策略配置信息：
  LST RAPAGINGRULE: MCC="123", MNC="03", LAC="156", RAC="12";
  ```
  %%LST RAPAGINGRULE: MCC="123", MNC="03", LAC="156", RAC="12";%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
         移动国家代码  =  123
             移动网号  =  03
           位置区域码  =  0x0156
           路由区域码  =  0x12
             星期序号  =  星期二
             起始时间  =  15:22
             终止时间  =  15:25
             T3313(s)  =  6
         N3313(times)  =  2
  重寻呼间隔递增值(s)  =  0
                 描述  =  noname
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于路由区的寻呼参数设置(LST-RAPAGINGRULE)_72345127.md`
