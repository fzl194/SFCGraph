---
id: UDG@20.15.2@MMLCommand@LST USERRUNINFO
type: MMLCommand
name: LST USERRUNINFO（显示运行信息进行收集配置用户）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USERRUNINFO
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 用户运行信息收集
status: active
---

# LST USERRUNINFO（显示运行信息进行收集配置用户）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

此命令用于显示当前被收集运行信息的所有用户，输出当前被收集运行信息的用户的IMSI/MSISDN。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/USERRUNINFO]] · 网关对IMSI/MSISDN指定的用户的运行信息进行收集配置（USERRUNINFO）

## 使用实例

- 系统中只有一条记录时，显示当前系统中进行信息记录的用户：
  ```
  LST USERRUNINFO:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  用户类型  =  IMSI
      IMSI  =  460011223344551
    MSISDN  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 系统中有多条记录时，显示当前系统中进行信息记录的用户：
  ```
  LST USERRUNINFO:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  用户类型    IMSI               MSISDN    

  IMSI        460011223344551    NULL      
  MSISDN      NULL               1223344551
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-USERRUNINFO.md`
