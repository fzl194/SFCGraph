---
id: UNC@20.15.2@MMLCommand@LST RRCINACTTAI
type: MMLCommand
name: LST RRCINACTTAI（查询RRC Inactive生效的TAI范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RRCINACTTAI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- RRC Inactive业务管理
- RRC Inactive生效的TAI范围
status: active
---

# LST RRCINACTTAI（查询RRC Inactive生效的TAI范围）

## 功能

**适用NF：AMF**

本命令用于查询RRC Inactive生效的TAI范围。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | MCC | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| BGNTAC | 跟踪区起始编码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RRCINACTTAI]] · RRC Inactive生效的TAI范围（RRCINACTTAI）

## 使用实例

- 查询RRC Inactive生效的TAI范围，执行如下命令：
  ```
  %%LST RRCINACTTAI:;%%
  RETCODE = 0  操作成功

  输出结果如下
  --------------
             MCC  =  123
             MNC  =  00
  跟踪区起始编码  =  000112
  跟踪区结束编码  =  000350
        描述信息  =  2
  (结果个数 = 1)

  ---    END
  ```
- 查询MCC为“123”，MNC为“00”条件下，RRC Inactive生效的TAI范围，执行如下命令：
  ```
  %%LST RRCINACTTAI: MCC="123", MNC="00";%%
  RETCODE = 0  操作成功

  输出结果如下
  --------------
             MCC  =  123
             MNC  =  00
  跟踪区起始编码  =  000112
  跟踪区结束编码  =  000350
        描述信息  =  2
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RRC-Inactive生效的TAI范围（LST-RRCINACTTAI）_23782778.md`
