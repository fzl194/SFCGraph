---
id: UDG@20.15.2@MMLCommand@LST POOLBINDGROUP
type: MMLCommand
name: LST POOLBINDGROUP（显示地址池与地址池组绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: POOLBINDGROUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池绑定地址池组
status: active
---

# LST POOLBINDGROUP（显示地址池与地址池组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询地址池组与地址池的绑定信息。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令指定地址池组名和地址池名时，表示显示指定地址池组和指定地址池之间的绑定信息。该命令指定地址池组名而不指定地址池名时，表示显示指定地址池组与所有和该地址池组绑定的地址池之间的绑定信息。该命令指定地址池名而不指定地址池组名时，表示显示指定地址池与所有和该地址池绑定的地址池组之间的绑定信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGROUPNAME | 地址池组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOLGROUP命令配置生成。 |
| POOLNAME | 地址池名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOL命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@POOLBINDGROUP]] · 地址池绑定地址池组中的地址池优先级（POOLBINDGROUP）

## 使用实例

- 查询名为poolgroup1的地址池组与名为pool1的地址池之间的绑定信息：
  ```
  LST POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="pool1";
  ```
  ```

  RETCODE = 0  操作成功。

  地址池与地址池组绑定关系
  --------------------------------
   地址池组名称  =  poolgroup1
         地址池名称  =  pool1
  地址池优先级  =  1
  (结果个数 = 1)
  ---    END
  ```
- 查询名为poolgroup1的地址池组与所有地址池之间的绑定信息：
  ```
  LST POOLBINDGROUP: POOLGROUPNAME="poolgroup1";
  ```
  ```

  RETCODE = 0  操作成功。

  地址池与地址池组绑定关系
  --------------------------------
  地址池组名称    地址池名称    地址池优先级

  poolgroup1         pool1        1               
  poolgroup1         pool3        10              
  (结果个数 = 2)
  ---    END
  ```
- 查询名为pool1的地址池与所有地址池组之间的绑定信息：
  ```
  LST POOLBINDGROUP: POOLNAME="pool1";
  ```
  ```

  RETCODE = 0  操作成功。

  地址池与地址池组绑定关系
  --------------------------------
  地址池组名称    地址池名称    地址池优先级

  poolgroup1        pool1         1               
  poolgroup3        pool1         6               
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-POOLBINDGROUP.md`
