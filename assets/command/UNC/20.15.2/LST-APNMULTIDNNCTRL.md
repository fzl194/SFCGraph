---
id: UNC@20.15.2@MMLCommand@LST APNMULTIDNNCTRL
type: MMLCommand
name: LST APNMULTIDNNCTRL（查询2B2C漫游双DNN特性APN级的相关功能控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNMULTIDNNCTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- APN粒度2B2C双DNN控制
status: active
---

# LST APNMULTIDNNCTRL（查询2B2C漫游双DNN特性APN级的相关功能控制）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询2B2C漫游双DNN特性APN级的相关功能控制。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2B2C漫游双DNN特性的通用DNN会话的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNMULTIDNNCTRL]] · 2B2C漫游双DNN特性APN级的相关功能控制（APNMULTIDNNCTRL）

## 使用实例

- 显示“APN名称”为“huawei.com”的2B2C漫游双DNN特性相关功能控制：
  ```
  %%LST APNMULTIDNNCTRL: APN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  --------
              APN名称  =  huawei.com
  在EPS是否先获取策略  =  使能
     专网会话触发方式  =  继承
    UE IP地址转换位置  =  继承
  园区DNN信元携带方式  =  继承
     是否支持就近接入  =  继承
  (结果个数 = 1)

  ---    END
  ```
- 显示全部APN的2B2C漫游双DNN特性相关功能控制：
  ```
  %%LST APNMULTIDNNCTRL:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称  	在EPS是否先获取策略  专网会话触发方式  UE IP地址转换位置  园区DNN信元携带方式  是否支持就近接入	
  huawei.com  	使能                 继承              继承               继承                 继承        
  huawei2.com    	使能                 继承              继承               继承                 继承        
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNMULTIDNNCTRL.md`
