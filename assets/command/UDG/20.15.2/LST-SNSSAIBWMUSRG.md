---
id: UDG@20.15.2@MMLCommand@LST SNSSAIBWMUSRG
type: MMLCommand
name: LST SNSSAIBWMUSRG（查询带宽管理用户组切片绑定）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SNSSAIBWMUSRG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理用户切片绑定
status: active
---

# LST SNSSAIBWMUSRG（查询带宽管理用户组切片绑定）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询一个带宽管理用户组下绑定的切片。当运营商希望查询某个带宽管理用户组下绑定的切片，则执行该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要被切片绑定的带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SNSSAIBWMUSRG]] · 带宽管理用户组切片绑定（SNSSAIBWMUSRG）

## 使用实例

- 假如运营商希望查询名为“test”的用户组下绑定的切片：
  ```
  LST SNSSAIBWMUSRG:USERGROUPNAME="test";
  ```
  ```

  RETCODE = 0  操作成功

  用户组切片绑定信息
  ------------------
     用户组名称  =  test
  切片/服务类型  =  1
     切片区分码  =  123456
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商希望查询所有用户组下绑定的切片：
  ```
  LST SNSSAIBWMUSRG:;
  ```
  ```

  RETCODE = 0  操作成功

  用户组切片绑定信息
  ------------------
  用户组名称  切片/服务类型  切片区分码  

  test        1              123456      
  test        2              654321      
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SNSSAIBWMUSRG.md`
