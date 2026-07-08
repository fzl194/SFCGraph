---
id: UNC@20.15.2@MMLCommand@LST INTFURPF
type: MMLCommand
name: LST INTFURPF（查询安全接口URPF）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTFURPF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略接口URPF
status: active
---

# LST INTFURPF（查询安全接口URPF）

## 功能

该命令用来查询接口的URPF配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/INTFURPF]] · 安全接口URPF（INTFURPF）

## 使用实例

- 查询SEC接口URPF：
  ```
  LST INTFURPF:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
     安全URPF检查类型  =  宽松
     安全匹配默认路由  =  接受
           安全协议族  =  IPv4
             接口名称  =  Ethernet66/0/3
  (结果个数 = 1)
  ---    END
  ```
- 查询指定条件SEC接口URPF：
  ```
  LST INTFURPF:IFNAME="Ethernet66/0/3";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
     安全URPF检查类型  =  宽松
     安全匹配默认路由  =  接受
           安全协议族  =  IPv4
             接口名称  =  Ethernet66/0/3
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询安全接口URPF（LST-INTFURPF）_49961702.md`
