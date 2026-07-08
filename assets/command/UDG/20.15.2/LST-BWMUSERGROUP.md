---
id: UDG@20.15.2@MMLCommand@LST BWMUSERGROUP
type: MMLCommand
name: LST BWMUSERGROUP（查询带宽管理用户组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BWMUSERGROUP
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
- 带宽管理用户组
status: active
---

# LST BWMUSERGROUP（查询带宽管理用户组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询带宽管理用户组。当运营商希望查询某用户组或所有用户组的名称、优先级、业务类型等参数时，执行该命令。

## 注意事项

如果不指定用户组名称，则查询所有已配置的用户组信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRYUSRGRPTYPE | 用户组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置带宽管理用户组的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEFAULT_GROUP：默认用户组。<br>- SPECIFIC_GROUP：特定用户组。<br>默认值：无<br>配置原则：无 |
| USERGROUPNAME | 用户组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QRYUSRGRPTYPE”配置为“SPECIFIC_GROUP”时为必选参数。<br>参数含义：该参数用于配置带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMUSERGROUP]] · 带宽管理用户组（BWMUSERGROUP）

## 使用实例

- 假如运营商需要查询名为“testbwmusergroup”的具体带宽管理用户组：
  ```
  LST BWMUSERGROUP: QRYUSRGRPTYPE=SPECIFIC_GROUP,USERGROUPNAME="testbwmusergroup";
  ```
  ```

  RETCODE = 0  操作成功。

  用户组信息
  ----------
            用户组名称  =  testbwmusergroup
            用户组类型  =  特定用户组
          用户组优先级  =  2
        用户级业务类型  =  Non TOS
      用户组级业务类型  =  Non TOS
            配置域名称  =  NULL
    用户级规则使能开关  =  使能
  用户组级规则使能开关  =  使能
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有带宽管理用户组：
  ```
  LST BWMUSERGROUP:;
  ```
  ```

  RETCODE = 0  操作成功。

  用户组信息
  ----------
  用户组名称          用户组类型    用户组优先级    用户级业务类型    用户组级业务类型    配置域名称    用户级规则使能开关    用户组级规则使能开关

  default             默认用户级    NULL            Non TOS           Non TOS             NULL          使能                  使能
  testbwmusergroup    特定用户组    2               Non TOS           Non TOS             NULL          使能                  使能
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询带宽管理用户组（LST-BWMUSERGROUP）_82837471.md`
