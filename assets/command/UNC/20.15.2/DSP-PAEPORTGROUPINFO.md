---
id: UNC@20.15.2@MMLCommand@DSP PAEPORTGROUPINFO
type: MMLCommand
name: DSP PAEPORTGROUPINFO（显示PAE端口组信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEPORTGROUPINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 端口
status: active
---

# DSP PAEPORTGROUPINFO（显示PAE端口组信息）

## 功能

该命令用于显示PAE端口组信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PAEPORTGROUPINFO]] · PAE端口组信息（PAEPORTGROUPINFO）

## 使用实例

- 显示微服务类型为“104”微服务实例为“csdb-pod-0172-16-1-200__103__0”的PAE端口组信息：
  ```
  %%DSP PAEPORTGROUPINFO: CELLTYPE="104", CELLINSTANCE="csdb-pod-0172-16-1-200__103__0";%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
    微服务类型  =  104
  微服务实例号  =  csdb-pod-0172-16-1-200__103__0
        组名称  =  default
          组ID  =  0
      平面类型  =  数据平面
      平面列表  =  0,1
    路由优先级  =  0
      组网模式  =  Trunk-BOND
  路由功能开关  =  路由优选功能开
  (结果个数 = 1)

  ---    END
  ```
- 显示所有PAE端口组信息：
  ```
  %%DSP PAEPORTGROUPINFO:;%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
  微服务类型  微服务实例号                                   组名称   组ID  平面类型  平面列表  路由优先级  组网模式    路由功能开关    
  
  104         udgctrl-pod-0172-16-0-42__103__0               default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开  
  104         csdb-pod-0172-16-1-200__103__0                 default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开  
  104         gcp-pod-0172-16-0-33__103__0                   default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开  
  104         sfm-pod-5c5786b9dd-mmp4x172-16-0-237__103__0   default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开 
  104         csdb-pod-1172-16-1-60__103__0                  default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开  
  104         udgctrl-pod-1172-16-0-188__103__0              default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开  
  104         sfm-pod-5c5786b9dd-n6nqm172-16-0-114__103__0   default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开    
  104         sfm-pod-5c5786b9dd-6spdg172-16-0-141__103__0   default  0     数据平面  0,1       0           Trunk-BOND  路由优选功能开    
  (结果个数 = 8)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEPORTGROUPINFO.md`
