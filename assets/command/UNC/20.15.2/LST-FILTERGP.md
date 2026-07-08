---
id: UNC@20.15.2@MMLCommand@LST FILTERGP
type: MMLCommand
name: LST FILTERGP（查询过滤组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FILTERGP
command_category: 查询类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- 过滤器组管理
status: active
---

# LST FILTERGP（查询过滤组）

## 功能

**适用NF：SMF**

此命令用于查询过滤组，可以指定过滤组的ID或名称来查询，也可以同时指定过滤组ID和名称。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERGPID | 过滤组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定过滤组唯一标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |
| FILTERGPNAME | 过滤组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定过滤组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FILTERGP]] · 过滤组（FILTERGP）

## 使用实例

- 运营商希望查看所有过滤组信息。
  ```
  %%LST FILTERGP:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  过滤组ID  =  1
  过滤组名  =  UPFILTER
  (结果个数 = 1)

   ----     END
  ```
- 运营商希望查看过滤组ID为1的过滤组信息。
  ```
  %%LST FILTERGP: FILTERGPID=1;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  过滤组ID  =  1
  过滤组名  =  UPFILTER
  (结果个数 = 1)

   ----     END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FILTERGP.md`
