---
id: UNC@20.15.2@MMLCommand@LST SBILINKCFG
type: MMLCommand
name: LST SBILINKCFG（查询SBI接口链路属性配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBILINKCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路属性管理
status: active
---

# LST SBILINKCFG（查询SBI接口链路属性配置）

## 功能

该命令用于查询服务化接口静态链路的配置信息和动态链路的属性配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务化接口链路的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~513。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SBI接口链路属性配置（SBILINKCFG）](configobject/UNC/20.15.2/SBILINKCFG.md)

## 使用实例

- 若运营商想查询索引为1的服务化接口静态链路的配置信息，可以执行如下命令：
  ```
  %%LST SBILINKCFG: INDEX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                        索引  =  1
                    链路类型  =  Dynamic
       服务化接口本端实体索引  =  1
                  对端NF类型  =  NFTypeNRF
                对端NF实例ID  =  bf33a517-7789-4637-b675-b3591b0d706b
              对端NF服务名称  =  nnssf-nsselection
            对端NF服务实例ID  =  1
                       模式  =  NULL
                     IP类型  =  NULL
            HTTP本端实体索引  =  0
               对端IPv4地址  =  0.0.0.0
               对端IPv6地址  =  ::
                   对端端口  =  0
          SBI链路集策略索引  =  1
                   网络信息  = NULL
                      描述  =  sbilink
  (结果个数 = 1)

  ---    END
  ```
- 若运营商想查询所有服务化接口链路的配置信息，可以用如下命令：
  ```
  %%LST SBILINKCFG:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                        索引  =  1
                    链路类型  =  Dynamic
       服务化接口本端实体索引  =  1
                  对端NF类型  =  NFTypeNRF
                对端NF实例ID  =  bf33a517-7789-4637-b675-b3591b0d706b
              对端NF服务名称  =  nnssf-nsselection
            对端NF服务实例ID  =  1
                       模式  =  NULL
                     IP类型  =  NULL
            HTTP本端实体索引  =  0
               对端IPv4地址  =  0.0.0.0
               对端IPv6地址  =  ::
                   对端端口  =  0
          SBI链路集策略索引  =  1
                   网络信息  = NULL
                      描述  =  sbilink
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SBI接口链路属性配置（LST-SBILINKCFG）_29291771.md`
