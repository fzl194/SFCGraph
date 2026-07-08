---
id: UNC@20.15.2@MMLCommand@LST NSMAPPARABYPLMN
type: MMLCommand
name: LST NSMAPPARABYPLMN（查询指定PLMN的网络切片映射参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSMAPPARABYPLMN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片映射管理
- 网络切片映射控制参数
status: active
---

# LST NSMAPPARABYPLMN（查询指定PLMN的网络切片映射参数）

## 功能

**适用NF：AMF**

该命令用于查询指定PLMN用户的网络切片映射相关参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于配置用户归属PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于配置用户归属PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSMAPPARABYPLMN]] · 指定PLMN的网络切片映射参数（NSMAPPARABYPLMN）

## 使用实例

查询MCC为“123”、MNC为“45”的用户的网络切片映射相关参数策略，执行如下命令：

```
%%LST NSMAPPARABYPLMN: MCC="123", MNC="45";%%
RETCODE = 0  操作成功

结果如下
--------
                 移动国家码  =  123
                   移动网号  =  45
           本地切片映射开关  =  打开
漫游用户CFG切片增强功能开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSMAPPARABYPLMN.md`
