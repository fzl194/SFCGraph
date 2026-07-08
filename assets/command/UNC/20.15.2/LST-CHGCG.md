---
id: UNC@20.15.2@MMLCommand@LST CHGCG
type: MMLCommand
name: LST CHGCG（查询CG配置参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGCG
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费控制
status: active
---

# LST CHGCG（查询CG配置参数）

## 功能

**适用网元：SGSN**

该命令用于查询CG相关配置。

## 注意事项

如果有输入参数，则显示与输入参数均匹配的CG配置记录；如果没有输入参数，则显示所有CG配置记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRO | GTP承载协议 | 可选必选说明：可选参数<br>参数含义：该参数用于指示CG支持的GTP'承载协议。<br>取值范围：<br>- “UDP(UDP)”<br>- “TCP(TCP)”<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGCG]] · CG配置参数（CHGCG）

## 使用实例

1. 查询所有的CG配置信息，配置格式为：
  LST CHGCG:;

  ```
  %%LST CHGCG:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  IP地址类型    CG的IPV4地址         优先级    GTP承载协议    CG协议版本    CG接收端口号    缺省CG    CG名  

  IPV4          10.141.149.100       0         UDP            R98           3386            是        noname
  IPV4          10.141.149.130       0         UDP            R98           3386            是        noname
  仍有后续报告输出
  ---    END

  %%LST CHGCG:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  IP地址类型    CG的IPV6地址                        优先级    GTP承载协议    CG协议版本    CG接收端口号    缺省CG    CG名  

  IPV6          2001:db8:10:19:44:55:10:12           0         UDP            R98           3386            是        noname
  IPV6          2001:db8:10:19:44:55:10:32           0         UDP            R98           3386            是        noname
  (结果个数 = 4)
  共有2个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGCG.md`
