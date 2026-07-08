---
id: UNC@20.15.2@MMLCommand@LST MDTPLMN
type: MMLCommand
name: LST MDTPLMN（查询基于管理的最小化路测的PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MDTPLMN
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- MDT管理
status: active
---

# LST MDTPLMN（查询基于管理的最小化路测的PLMN）

## 功能

**适用网元：MME**

该命令用于查询基于管理的最小化路测（MDT）的PLMN。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数表示组成Serving PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数表示组成Serving PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MDTPLMN]] · 基于管理的最小化路测的PLMN（MDTPLMN）

## 使用实例

查询所有最小化路测的PLMN，执行如下命令：

LST MDTPLMN :;

```
%%LST MDTPLMN:;%% 
RETCODE = 0  操作成功  
操作结果如下 
------------------------ 
移动国家码        移动网号              描述信息   
123                  030                  visit         
456                  030                  visit         
(结果个数 = 2)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于管理的最小化路测的PLMN(LST-MDTPLMN)_63157190.md`
