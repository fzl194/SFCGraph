---
id: UNC@20.15.2@MMLCommand@LST USERPROFILE
type: MMLCommand
name: LST USERPROFILE（查询用户模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USERPROFILE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# LST USERPROFILE（查询用户模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询用户模板。

## 注意事项

如果不输入用户模板名称，表示查询系统中所有用户模板。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPSPECTYPE | 用户模板规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板规格类型，当取值为SPECIFICATION_LIMITED时，表示规格受限用户模板，表示用户安装的该类型用户模板数和该类型用户模板绑定的规则数量均比默认规格小，需要配合相应特性使用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USERPROFILE]] · 用户模板（USERPROFILE）

## 使用实例

- 假如运营商需要查询名称为testuserprofilename的用户模板：
  ```
  LST USERPROFILE: USERPROFILENAME="testuserprofilename";
  ```
  ```

  RETCODE = 0  操作成功

  用户模板信息
  ------------
                      用户模板名称  =  testuserprofilename
              免费业务在线计费标识  =  使能
              免费业务离线计费标识  =  使能
                          锁定标记  =  不使能
                     缺省URR组名称  =  NULL
                初始请求URR组名称1  =  NULL
                初始请求URR组名称2  =  NULL
                初始请求URR组名称3  =  NULL
                初始请求URR组名称4  =  NULL
                初始请求URR组名称5  =  NULL
                初始请求URR组名称6  =  NULL
                初始请求URR组名称7  =  NULL
                初始请求URR组名称8  =  NULL
                初始请求URR组名称9  =  NULL
               初始请求URR组名称10  =  NULL
                      用户模板类型  =  PCC
              免费业务融合计费标识  =  使能
                      模板生效范围  =  对中心和边缘UPF均生效
                  用户模板规格类型  =  默认配置
                      质差分析开关  =  不使能
  免费在线业务携带在线相关标识开关  =  继承
                      媒体中继开关  =  不使能
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有的用户模板：
  ```
  LST USERPROFILE:;
  ```
  ```

  RETCODE = 0  操作成功

  用户模板信息
  ------------
  用户模板名称         免费业务在线计费标识  免费业务离线计费标识  锁定标记  缺省URR组名称  初始请求URR组名称1  初始请求URR组名称2  初始请求URR组名称3  初始请求URR组名称4  初始请求URR组名称5  初始请求URR组名称6  初始请求URR组名称7  初始请求URR组名称8  初始请求URR组名称9  初始请求URR组名称10  用户模板类型  免费业务融合计费标识  模板生效范围           用户模板规格类型  质差分析开关  免费在线业务携带在线相关标识开关  媒体中继开关
 
  testuserprofilename  使能                  使能                  不使能    NULL           NULL                NULL                NULL                NULL                NULL                NULL                NULL                NULL                NULL                NULL                 PCC           使能                  对中心和边缘UPF均生效  默认配置          不使能    继承 不使能
  userprofile1         使能                  使能                  不使能    NULL           NULL                NULL                NULL                NULL                NULL                NULL                NULL                NULL                NULL                NULL                 PCC           使能                  对中心和边缘UPF均生效  默认配置          不使能    继承 不使能
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USERPROFILE.md`
