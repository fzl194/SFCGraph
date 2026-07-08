---
id: UDG@20.15.2@MMLCommand@LST RPTPROTOCOLMAP
type: MMLCommand
name: LST RPTPROTOCOLMAP（查询业务报表承载协议映射配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTPROTOCOLMAP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表本地策略管理
- 业务报表承载协议映射
status: active
---

# LST RPTPROTOCOLMAP（查询业务报表承载协议映射配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询业务报表承载协议映射信息。当运营商希望查询业务报表承载协议映射信息时，则执行该命令。

## 注意事项

如果不输入任何参数，则查询系统所有配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指示配置的协议组、协议级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于设置协议名称。数据源为UPF支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为UPF支持识别的默认协议、子协议，可以通过工程命令display protocol-list查询。 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于设置协议组名称。数据源为UPF支持识别的所有默认协议组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为UPF支持识别的默认协议组，可以通过工程命令display protocol-list查询。 |
| MPPROTCLASSNM | 映射承载协议分类名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置映射承载协议分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD RPTPROTMPCLASS命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPROTOCOLMAP]] · 业务报表映射承载协议分类配置（RPTPROTOCOLMAP）

## 使用实例

- 假如运营商需要查询p2p映射协议分类的业务报表承载协议映射信息：
  ```
  LST RPTPROTOCOLMAP: MPPROTCLASSNM="p2p";
  ```
  ```

  RETCODE = 0  操作成功。

  业务报表承载协议映射信息：
  --------------------
              协议等级  =  Protocol Group
              协议名称  =  NULL
            协议组名称  =  p2p
  映射承载协议分类名称  =  p2p
  映射承载协议分类索引  =  20
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询所有业务报表承载协议映射信息：
  ```
  LST RPTPROTOCOLMAP:;
  ```
  ```

  RETCODE = 0  操作成功。

  业务报表承载协议映射信息：
  --------------------
  协议等级          协议名称    协议组名称    映射承载协议分类名称   映射承载协议分类索引
  Protocol Group    NULL        p2p           p2p                    20
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RPTPROTOCOLMAP.md`
