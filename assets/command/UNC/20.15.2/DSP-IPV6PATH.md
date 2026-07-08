---
id: UNC@20.15.2@MMLCommand@DSP IPV6PATH
type: MMLCommand
name: DSP IPV6PATH（查询IPv6 Path信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPV6PATH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- IPV6
status: active
---

# DSP IPV6PATH（查询IPv6 Path信息）

## 功能

该命令用于查询查看IPv6 Path信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6PATH]] · IPv6 Path信息（IPV6PATH）

## 使用实例

- 显示单条IPv6 Path信息：
  ```
  DSP IPV6PATH:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                PATH ID  =  0
               PATH状态  =  3
           PATH中断原因  =  0
  发送至下一个组件的PID  =  0
               下一段ID  =  0
                VPN索引  =  0
               发送标记  =  0
               扩展标记  =  0
               实例标记  =  0
             源IPv6地址  =  2001:db8::1
           目的IPv6地址  =  2001:db8::2
             入接口索引  =  8
       指定的出接口索引  =  0
     指定下一条IPv6地址  =  ::
             TUNNEL类型  =  0
              TUNNEL ID  =  0
                 XC索引  =  0
             PP6组件PID  =  7471119
             PP6组件CID  =  2154954772
  (结果个数 = 1)
  ---    END
  ```
- 显示多条IPv6 Path信息：
  ```
  DSP IPV6PATH:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  PATH ID    PATH状态    PATH中断原因    发送至下一个组件的PID    下一段ID    VPN索引    发送标记    扩展标记    实例标记    源IPv6地址    目的IPv6地址    入接口索引    指定的出接口索引    指定下一条IPv6地址    TUNNEL类型    TUNNEL ID    XC索引    PP6组件PID    PP6组件CID

  1          3           0               7471119                  67109408    0          5           0           2           2001:db8::1   2001:db8::2     8             0                   ::                    0             0            0         7471119       2154954772
  0          3           0               7471119                  67109408    0          5           0           0           2001:db8::3   2001:db8::4     13            0                   ::                    0             0            0         7471119       2154954772
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-IPV6PATH.md`
