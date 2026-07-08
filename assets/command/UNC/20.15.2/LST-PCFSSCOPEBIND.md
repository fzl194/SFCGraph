---
id: UNC@20.15.2@MMLCommand@LST PCFSSCOPEBIND
type: MMLCommand
name: LST PCFSSCOPEBIND（查询PCF业务服务区的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCFSSCOPEBIND
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF业务服务区绑定
status: active
---

# LST PCFSSCOPEBIND（查询PCF业务服务区的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询PCF业务服务区的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BINDNAME | 绑定名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定记录的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |
| SSCOPEID | 服务区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务区标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：<br>配置的SSCOPEID必须是ADD PCFSSCOPE命令已配置的SSCOPEID。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCFSSCOPEBIND]] · PCF业务服务区的绑定关系（PCFSSCOPEBIND）

## 使用实例

- 查询BINDNAME为towna的记录。
  ```
  LST PCFSSCOPEBIND: BINDNAME="towna";
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```
- 查询SSCOPEID为citya的记录。
  ```
  LST PCFSSCOPEBIND: SSCOPEID="citya";
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```
- 查询BINDNAME为towna，SSCOPEID为citya的记录。
  ```
  LST PCFSSCOPEBIND: BINDNAME="towna", SSCOPEID="citya";
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```
- 查询所有记录。
  ```
  LST PCFSSCOPEBIND:;
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCFSSCOPEBIND.md`
