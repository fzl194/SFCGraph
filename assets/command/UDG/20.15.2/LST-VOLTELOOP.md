---
id: UDG@20.15.2@MMLCommand@LST VOLTELOOP
type: MMLCommand
name: LST VOLTELOOP（查询VoLTE话路环回功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VOLTELOOP
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VOLTE管理
- Volte环回
status: active
---

# LST VOLTELOOP（查询VoLTE话路环回功能）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

此命令用于查询VoLTE话路环回功能的当前配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VOLTELOOP]] · VoLTE话路环回功能（VOLTELOOP）

## 使用实例

- 查询VoLTE话路环回配置信息(当仅配置了一条信息时)：
  ```
  LST VOLTELOOP:;
  ```
  ```

  RETCODE = 0  操作成功。

  VOLTE环回信息
  -------------
  标识类型  =  IMSI
      IMSI  =  456645645644565
    环回点  =  上行入方向
    MSISDN  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询VoLTE话路环回配置信息(当配置了多条信息时)：
  ```
  LST VOLTELOOP:;
  ```
  ```

  RETCODE = 0  操作成功。

  VOLTE环回信息
  -------------
  标识类型    IMSI               环回点        MSISDN

  IMSI        356897584584516    上行出方向    NULL  
  IMSI        456645645644565    上行入方向    NULL  
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VOLTELOOP.md`
