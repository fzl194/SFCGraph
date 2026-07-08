---
id: UDG@20.15.2@MMLCommand@LST USRRELATEIDEN
type: MMLCommand
name: LST USRRELATEIDEN（查询用户关联识别）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USRRELATEIDEN
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 用户关联识别
status: active
---

# LST USRRELATEIDEN（查询用户关联识别）

## 功能

**适用NF：PGW-U、UPF**

当运营商需要查询特定协议的用户关联功能，显示指定protocol的用户关联识别配置时配置该命令，该命令支持显示所有的用户关联识别配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置对应的协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议，可以通过工程命令smctrldsp protocol-list查询。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USRRELATEIDEN]] · 用户关联识别（USRRELATEIDEN）

## 使用实例

- 查询一个指定的协议https的用户关联识别功能配置信息：
  ```
  LST USRRELATEIDEN: PROTOCOLNAME="https";
  ```
  ```

  RETCODE = 0  操作成功

  用户关联识别信息
  ----------------
          协议名称  =  https
  用户关联识别开关  =  使能
        配置域名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有配置过的用户关联功能配置信息：
  ```
  LST USRRELATEIDEN:;
  ```
  ```
  %%
  RETCODE = 0  操作成功

  用户关联识别信息
  ----------------
  协议名称    用户关联识别开关  配置域名称

  7tv_data    使能              NULL
  https       使能              NULL
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-USRRELATEIDEN.md`
