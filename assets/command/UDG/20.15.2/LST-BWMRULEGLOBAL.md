---
id: UDG@20.15.2@MMLCommand@LST BWMRULEGLOBAL
type: MMLCommand
name: LST BWMRULEGLOBAL（查询全局带宽管理规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BWMRULEGLOBAL
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
- 带宽管理规则
status: active
---

# LST BWMRULEGLOBAL（查询全局带宽管理规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询全局业务带宽控制规则。当运营商希望查询全局的某个或全部带宽管理规则的业务类型和控制器等参数信息时，则执行该命令。

## 注意事项

如果不指定带宽管理规则名称，则查询所有的全局业务带宽管理规则。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMRULENAME | 带宽管理规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置带宽管理规则的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMRULEGLOBAL]] · 全局带宽管理规则（BWMRULEGLOBAL）

## 使用实例

- 假如运营商需要查询名为“testbwmruleglobal”的全局带宽管理规则：
  ```
  LST BWMRULEGLOBAL:BWMRULENAME="testbwmruleglobal";
  ```
  ```

  RETCODE = 0  操作成功。

  全局带宽管理规则信息
  --------------------
                用户组名称  =  global
          带宽管理规则名称  =  testbwmruleglobal
          带宽管理规则类型  =  全局级别特定
        带宽管理规则优先级  =  5
          带宽控制业务名称  =  bs1
  上行带宽管理控制器名称一  =  bc2
  下行带宽管理控制器名称一  =  bwmc
              时间段名称一  =  NULL
  上行带宽管理控制器名称二  =  NULL
  下行带宽管理控制器名称二  =  NULL
              时间段名称二  =  NULL
  上行带宽管理控制器名称三  =  NULL
  下行带宽管理控制器名称三  =  NULL
              时间段名称三  =  NULL
  上行带宽管理控制器名称四  =  NULL
  下行带宽管理控制器名称四  =  NULL
              时间段名称四  =  NULL
                  业务级别  =  1
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询所有全局带宽管理规则：
  ```
  LST BWMRULEGLOBAL:;
  ```
  ```

  RETCODE = 0  操作成功

  全局带宽管理规则信息
  --------------------
  用户组名称  带宽管理规则名称  带宽管理规则类型  带宽管理规则优先级  带宽控制业务名称  上行带宽管理控制器名称一  下行带宽管理控制器名称一  时间段名称一  上行带宽管理控制器名称二  下行带宽管理控制器名称二  时间段名称二  上行带宽管理控制器名称三  下行带宽管理控制器名称三  时间段名称三  上行带宽管理控制器名称四  下行带宽管理控制器名称四  时间段名称四  业务级别  

  global      bwmrule1          全局级别特定      1                   bwmservice1       bwmctrl1                  bwmctrl2                  NULL          NULL                      NULL                      NULL          NULL                      NULL                      NULL          NULL                      NULL                      NULL          1         
  global      bwmrule2          全局级别特定      2                   bwmservice2       bwmctrl1                  bwmctrl2                  NULL          NULL                      NULL                      NULL          NULL                      NULL                      NULL          NULL                      NULL                      NULL          1         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-BWMRULEGLOBAL.md`
