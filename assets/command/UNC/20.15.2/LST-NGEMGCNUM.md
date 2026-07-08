---
id: UNC@20.15.2@MMLCommand@LST NGEMGCNUM
type: MMLCommand
name: LST NGEMGCNUM（查询紧急号码配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGEMGCNUM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G 语音业务管理
- 紧急呼叫业务管理
- 紧急呼叫号码配置
status: active
---

# LST NGEMGCNUM（查询紧急号码配置信息）

## 功能

**适用NF：AMF**

此命令用于查询紧急号码的配置。

## 注意事项

如果没有输入参数，查询所有的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要配置紧急呼叫号码的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NUM | 紧急呼叫号码 | 可选必选说明：可选参数<br>参数含义：该参数用于指明紧急业务对应的号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~80。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| ESC | 紧急服务分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急呼叫号码的服务类型。<br>数据来源：全网规划<br>取值范围：<br>- “POLICE（报警）”：报警<br>- “AMBULANCE（医疗救护）”：医疗救护<br>- “FIREBRIGADE（火警）”：火警<br>- “MARINEGUARD（海上救援）”：海上救援<br>- “MOUNTAIN（高山救援）”：高山救援<br>- “ALL（通用类型）”：通用类型<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGEMGCNUM]] · 紧急号码配置信息（NGEMGCNUM）

## 使用实例

- 查询所有的移动国家码下配置的紧急呼叫号码，执行如下命令：
  ```
  %%LST NGEMGCNUM:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    移动国家码  =  460
  紧急呼叫号码  =  119
  紧急服务分类  =  火警
  (结果个数 = 1)

  ---    END
  ```
- 查询“移动国家码”为“460”时配置的紧急呼叫号码，执行如下命令：
  ```
  %%LST NGEMGCNUM: MCC="460";%%
  RETCODE = 0  操作成功

  结果如下
  --------
    移动国家码  =  460
  紧急呼叫号码  =  110
  紧急服务分类  =  报警
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询紧急号码配置信息（LST-NGEMGCNUM）_09653760.md`
