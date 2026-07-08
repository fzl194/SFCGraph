---
id: UDG@20.15.2@MMLCommand@LST CHRRPTAPN
type: MMLCommand
name: LST CHRRPTAPN（查询所有基于APN的CHR本地存盘策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CHRRPTAPN
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 呼叫日志管理
- 基于APN的CHR本地存盘配置
status: active
---

# LST CHRRPTAPN（查询所有基于APN的CHR本地存盘策略）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示所有基于APN的CHR本地存盘策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHRRPTAPN]] · 指定某个APN做本地存储CHR表单的策略（CHRRPTAPN）

## 使用实例

- 显示一个基于APN的CHR本地存盘策略信息：
  ```
  LST CHRRPTAPN:;
  ```
  ```
  %%
  RETCODE = 0 操作成功。

  基于APN的CHR本地存盘策略
  -------------------
       APN = apn1.com
  CHR 类型 = 信令CHR
   会话数量 = 3
  (结果个数 = 1)
  --- END
  ```
- 显示多个基于APN的CHR本地存盘策略信息：
  ```
  LST CHRRPTAPN:;
  ```
  ```

  RETCODE = 0 操作成功。

  基于APN的CHR本地存盘策略
  -------------------
  APN              CHR 类型    会话数量
  apn1.com     Signal CHR      1
  apn2.com     Signal CHR      1
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CHRRPTAPN.md`
