---
id: UDG@20.15.2@MMLCommand@LST UPDIAMRTREALM
type: MMLCommand
name: LST UPDIAMRTREALM（查询Diameter路由域名信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDIAMRTREALM
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- 路由管理
- Diameter路由
status: active
---

# LST UPDIAMRTREALM（查询Diameter路由域名信息）

## 功能

**适用NF：UPF**

该命令用于查看已配置的Diameter路由相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMRTREALM]] · Diameter路由域名信息（UPDIAMRTREALM）

## 使用实例

- 显示指定realm名的Diameter路由参数，realm名为“example.com”：
  ```
  LST UPDIAMRTREALM:REALMNAME="example.com";
  ```
  ```

  RETCODE = 0  操作成功
  Diameter路由信息
  ----------------
  Diameter域名名称  =  example.com
      Diameter应用  =  SWM
      路由选择模式  =  主备
      Failover开关  =  允许
      自动倒回开关  =  允许
  (结果个数 = 1)
  ---    END
  ```
- 显示所有Diameter路由信息：
  ```
  LST UPDIAMRTREALM:;
  ```
  ```

  RETCODE = 0  操作成功
  Diameter路由信息
  ----------------
  Diameter域名名称  Diameter应用  路由选择模式  Failover开关  自动倒回开关  
  default           SWM           基于会话轮循  禁止          禁止          
  example.com       SWM           主备          允许          允许          
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Diameter路由域名信息（LST-UPDIAMRTREALM）_45195196.md`
